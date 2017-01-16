import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

nlocation = "/Users/nolanbonnie/Desktop/Python/chromedriver"
elocation = ""
llocation = "/Users/"+input("What USER")+"/Downloads/chromedriver"

loc = input("Who is using the code? (if CSF, csf)")
if loc == "nolan":
    driver = webdriver.Chrome(nlocation)
elif loc == "eric":
    driver = webdriver.Chrome(elocation)
elif loc == "luke":
    driver = webdriver.Chrome(llocation)
elif loc == "csf":
    driver = webdriver.Chrome(llocation)#input("Enter path of the chromedriver: "))
else:
    print("input not recognized")

driver.get("https://docs.google.com/spreadsheets/d/1ch5pT5ywKXvINhlhDJzvdl0YgxRjSdHKPzIf-ht5qgw/edit#gid=1772866043")
if loc == "nolan":
#Input Email--------------------------------------------------
    elem = driver.find_element_by_name('Email')
    elem.send_keys('nrbmee@gmail.com')
    elem.send_keys(Keys.RETURN)
#Input Password--------------------------------------------------
    time.sleep(.5)
    elem = driver.find_element_by_name('Passwd')
    elem.send_keys("chase5135")
    elem.send_keys(Keys.RETURN)

if loc == "luke":
#Input Email--------------------------------------------------
    elem = driver.find_element_by_name('Email')
    elem.send_keys('ljelissiry')
    elem.send_keys(Keys.RETURN)
#Input Password--------------------------------------------------
    time.sleep(.2)
    elem = driver.find_element_by_name('Passwd')
    elem.send_keys("lj2gmail16")
    elem.send_keys(Keys.RETURN)

if loc == "csf":
    #Input Email--------------------------------------------------
    elem = driver.find_element_by_name('Email')
    elem.send_keys('srv.csf')
    elem.send_keys(Keys.RETURN)
#Input Password--------------------------------------------------
    time.sleep(.5)
    elem = driver.find_element_by_name('Passwd')
    elem.send_keys("SRV2016CSF")#input("Enter CSF Google Password"))
    elem.send_keys(Keys.RETURN)

#CSF Class Lists (6 digit code)
List1 = "MACBCP ROESAP SSAGAP SCPCAP ENERW*"
List1 = List1.split(" ")

List2 = "VACSPP"
List2 = List2.split(" ")

List3 = ""
List3 = List3.split(" ")

ClassList = List1 + List2 + List3

startrow = int(input("First Row: "))
endrow = int(input("Last Row: "))
rnge = endrow - startrow

time.sleep(2)

scroll = startrow - 1
for v in range(scroll):
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
for v in range(3):
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

#String text = driver.findElement(By.id("some id")).get_attribute("attribute")

#Comparing Google Sheets Input with Transcript
for r in range(rnge):
    elem = driver.find_element_by_class_name('cell-input')
    SheetsFirstName = elem.get_attribute('innerText')[:-1]
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    elem = driver.find_element_by_class_name('cell-input')
    SheetsLastName = elem.get_attribute('innerText')[:-1]
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    elem = driver.find_element_by_class_name('cell-input')
    SheetsID = int(elem.get_attribute('innerText'))
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    elem = driver.find_element_by_class_name('cell-input')
    SheetsGrade = int(elem.get_attribute('innerText'))
    for v in range(5):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    elem = driver.find_element_by_class_name('cell-input')
    transcriptlink = elem.get_attribute('innerText')[:-1]

    driver.execute_script("window.open('" + transcriptlink + "', 'new_window')")
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(1)
    
    transcript = "NO"
    Classes = []
    reason = ""

    elem = driver.find_elements_by_class_name('drive-viewer-paginated-page-reader-block')
    if elem != []:
        TranscriptText = []
        for i in range(len(elem)):
            text = elem[i]
            TranscriptText.append(text.get_attribute('innerText'))
        TranscriptLastName = TranscriptText[-5].split(",")[0]

        elem = TranscriptText[1]
        TranscriptID = int(elem.split(" ")[2])
        TranscriptGrade = int(elem.split(" ")[4])

        if TranscriptLastName == SheetsLastName:
            if TranscriptID == SheetsID:
                if TranscriptGrade == SheetsGrade:
                    transcript = "YES"
                else:
                    reason = "Grade does not match"
            else:
                reason = "ID does not match"
        else:
            reason = "Name does not match"
    else:
        reason = "Transcript link is broken"

# locates classes and grades for most recent term from TranscriptText and stores in Classes
    if transcript == "YES":
        start = 0
        end = 0
        for i in range(len(TranscriptText)):
            if "2016-2017" in TranscriptText[i]:
                start = i + 1
            if "Credit: " in TranscriptText[i]:
                end = i
        CurrentTerm = " ".join(TranscriptText[start:end])
        CurrentTerm = CurrentTerm.replace("+","").replace("-","")
        CurrentTerm = CurrentTerm.split(" ")
        for i in range(len(CurrentTerm)):
            if CurrentTerm[i] in ClassList:
                Classes.append(CurrentTerm[i])
                n = 0
                while n >= 0:
                    n += 1
                    if "." in CurrentTerm[i+n]:
                        Grade = CurrentTerm[i+n-1]
                        if Grade == "A":
                            Grade = 3
                        elif Grade == "B":
                            Grade = 1
                        elif Grade == "C":
                            Grade = 0
                        else:
                            Grade = -1
                            transcript = "NO"
                            reason = "D or F in a course"
                        Classes.append(Grade)
                        n = -1
    if transcript == "YES":
        NumAPH = 0
        for List in [List1,List2,List3]:
            for Grade in range(4,0,-1):
                for Class in range(0,len(Classes),2):
                    if NumAPH < 2 and Classes[Class] in List and Classes[Class + 1] == Grade and \
                        (Classes[Class][5] == "P" or Classes[Class][5] == "H"):
                        Classes[Class + 1] = Classes[Class + 1] + 1
                        NumAPH += 1
        ClassesLeft = Classes[:]
        NumClasses = 0
        NumPoints = 0
        
    if transcript == "YES":
        NumClassesbyList = 0
        for Grade in range(4,-1,-1):
            for Class in range(len(ClassesLeft)-2,-1,-2):
                if ClassesLeft[Class] in List1 and \
                   ClassesLeft[Class + 1] == Grade and \
                   NumClassesbyList < 2 and NumClasses < 5:
                    NumClasses += 1
                    NumPoints += ClassesLeft[Class + 1]
                    NumClassesbyList += 1
                    del ClassesLeft[Class + 1]
                    del ClassesLeft[Class]
        if NumClasses < 2:
            transcript = "NO"
            reason = "< 2 List I courses"
        if NumPoints < 4:
            transcript = "NO"
            reason = "< 4 points from List I"

    if transcript == "YES":
        NumClassesbyList = 0
        for Grade in range(4,-1,-1):
            for Class in range(len(ClassesLeft)-2,-1,-2):
                if (ClassesLeft[Class] in List1 or ClassesLeft[Class] in List2) and \
                   ClassesLeft[Class + 1] == Grade and \
                   NumClassesbyList < 1 and NumClasses < 5:
                    NumClasses += 1
                    NumPoints += ClassesLeft[Class + 1]
                    NumClassesbyList += 1
                    del ClassesLeft[Class + 1]
                    del ClassesLeft[Class]
        if NumClasses < 3:
            transcript = "NO"
            reason = "< 3 List I & II courses"
        if NumPoints < 7:
            transcript = "NO"
            reason = "< 7 points from List I & II"

    if transcript == "YES":
        for Grade in range(4,-1,-1):
            for Class in range(len(ClassesLeft)-2,-1,-2):
                if ClassesLeft[Class] in ClassList and \
                   ClassesLeft[Class + 1] == Grade and \
                   NumClasses < 5:
                    NumClasses += 1
                    NumPoints += ClassesLeft[Class + 1]
                    del ClassesLeft[Class + 1]
                    del ClassesLeft[Class]
        if NumPoints < 10:
            transcript = "NO"
            reason = "< 10 points from List I, II, & III"


    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    ActionChains(driver) \
        .send_keys(Keys.ARROW_RIGHT) \
        .perform()

    actions = ActionChains(driver)
    actions.send_keys(Keys.DELETE,Keys.ENTER)
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(transcript)
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()

    actions = ActionChains(driver)
    actions.send_keys(Keys.DELETE,Keys.ENTER)
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(reason)
    actions.perform()
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    for v in range(9):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_LEFT)
        actions.perform()

    print("\n","Row: ",startrow + r,sep="")
    print(SheetsFirstName,SheetsLastName)
    if Classes != []:
        print(Classes)
    print("Transcript:",transcript)
    if reason != "":
        print("Reason:",reason)
