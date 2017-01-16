import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

nlocation = "/Users/nolanbonnie/Desktop/Python/chromedriver"
elocation = ""
llocation = "/Users/Luke/Downloads/chromedriver"

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


driver.get("https://docs.google.com/spreadsheets/d/1ch5pT5ywKXvINhlhDJzvdl0YgxRjSdHKPzIf-ht5qgw/edit#gid=1082589385")
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

startrow = int(input("What row do you want to start on?"))
endrow = int(input("What row do you want to end on?"))
rnge = endrow - startrow

#String text = driver.findElement(By.id("some id")).get_attribute("attribute")

#Comparing Google Sheets Input with Transcript
for i in range(rnge):
    scroll = startrow - 1 + i
    for v in range(scroll):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
    for v in range(4):
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
    transcriptlink = elem.get_attribute('innerText')
    driver.get(transcriptlink)

    transcript = "NO"
    reason = ""

    elem = driver.find_elements_by_class_name('drive-viewer-paginated-page-reader-block')
    TranscriptText = []
    for i in range(len(elem)):
        text = elem[i]
        TranscriptText.append(text.get_attribute('innerText'))
    print(TranscriptText)
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

    if transcript == "YES":
        start = 0
        end = 0
        for i in range(len(TranscriptText)):
            if "2016-2017" in TranscriptText[i]:
                start = i
            if "Credit: " in TranscriptText[i]:
                end = i
        CurrentGrades = " ".join(TranscriptText[start:end])
        CurrentGrades = CurrentGrades.replace("+","").replace("-","")
        Classes = CurrentGrades.split(" ")
        ClassList = ['MACBCP'] #Luke, input all codes here
        print(CurrentGrades)
        for x in range(len(Classes)):
            if len(Classes[x]) == 6:
                for i in range(len(ClassList)):
                    if ClassList[i] == Classes[x]:
                        print(ClassList[i], Classes[x], "Match")
                        for z in range(len(Classes)):
                            if Classes[z] == "5.0000" or Classes[z] == "4.0000" or Classes[z] == "3.0000" or Classes[z] == "2.0000" or Classes[z] == "1.0000":
                                Grade = Classes[z - 1]
                                print(Grade)
                    else:
                        print("invalid")
        
                        

