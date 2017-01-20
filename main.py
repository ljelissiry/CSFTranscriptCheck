import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#----------------------------------------------------------------------
#       Important Info to Change
#----------------------------------------------------------------------

SchoolYear = "2016-2017"
# School year of grades to check

TermNum = "1"
# Term number of grades to check

if input("Real (r) or Fake (f) transcript? ") == "r":
    GoogleSheet = "https://docs.google.com/spreadsheets/d/1T8HZYhpwB0LCP9Asbqa9mZ_YDAxuqARJ9yysrGrVi2I/edit#gid=167389222"
else:
    GoogleSheet = "https://docs.google.com/spreadsheets/d/1ch5pT5ywKXvINhlhDJzvdl0YgxRjSdHKPzIf-ht5qgw/edit#gid=1772866043"
# Link of Google Sheet

SleepTime = 1
# Time it gives to open transcript


#----------------------------------------------------------------------
#       CSF Class Lists
#----------------------------------------------------------------------


#CSF Class Lists (6 digit code obtained from course catalogs)
#appear in order of classes HERE: https://goo.gl/hQ8Jtg

EnglishClasses = "ENE9** ENE10* ENE10U ENE11* ENLCAP ENE12* ENERW* ENELAP"
LanguageClasses = "FLF1** FLF2** FLF3** FLF4*H FLFLAP FLS1** FLS2** FLS3** FLS4*H FLSLAP"
MathClasses = "MAA1** MAG*** MAA2** MATMA* MATMAH MAC*** MACABP MACBCP MAS*** MAS*AP MAAMT*"
ScienceClasses = "SCAP** SCAP*H SCB*** SCAB** SCB*AP SCC*** SCC**H SCC*AP ROESAP SCMB** SCP*** SCP**H SCPCAP"
SocialScienceClasses = "SSAG** SSAGPH SSAGAP SSE*** SSEMIP SSEMAP SSEHAP SSUS** SSUSAP SSWH**"

List1 = EnglishClasses + " " + LanguageClasses + " " + MathClasses + " " + \
        ScienceClasses + " " + SocialScienceClasses
List1 = List1.split(" ")

EnglishClasses = "NDCW*N NDJ1** NDJ2** NDSD**"
MathClasses = "MAAE1* MAAE2*"
ScienceClasses = "SCLS*N SCIPS*"
SocialScienceClasses = "SSCH** SSHWA* SSHGAP SSL*** SSP*** SSP*AP SSVE** SSWG** SSWW2*"
MusicClasses = "FAMTAP"
ComputerClasses = "VAC1*N VAC2** VAC*AP VACSPP VACPL*"

List2 = EnglishClasses + " " + LanguageClasses + " " + MathClasses + " " + \
        ScienceClasses + " " + SocialScienceClasses + " " + \
        MusicClasses + " " + ComputerClasses
List2 = List2.split(" ")

IndustrialArts = "ROAF*N VAAU1N VAAU2N ROAUTN VABBRN"
HomeEconomics = "VACA1N VACA2N"
PerformingArts = "FAD1** FAD2** FAD3** FAD4** FAD5** FATA1* FATA2* FATA3* FATA4* FATP** FAOI**"
Business = "VAIBE* MAPF*N"
VisualArts = "FA3D1* FA3D2* FA3D3N FAA1** FAA2** FAA5** ROCGA* ROWEB* FAP*** FAPA** FASAAP FAAV1* FAAV2*"
VocalMusic = "FACS** FACC** FAME** FATC** FAWE**"
InstrumentalMusic = "FACB** FAJB** FAJE** FAMB*N FAO*** FASB**"
Other = "NDAVID NDASS* NDH**N Leadership NDPUB NDAP** VAWX*N VAWXZN"
ROP = "ROIE** ROCITN ROCT2* ROSM** ROSMAN"

List3 = IndustrialArts + " " + HomeEconomics + " " + PerformingArts + " " + \
        Business + " " + VisualArts + " " + VocalMusic + " " + \
        InstrumentalMusic + " " + Other + " " + ROP
List3 = List3.split(" ")

ClassList = List1 + List2 + List3


#----------------------------------------------------------------------
#       Signing in to Google account
#----------------------------------------------------------------------


account = input("Google Account (if CSF, srv.csf): ")
if account == "srv.csf":
    password = "SRV2016CSF"
elif account == "luke":
    account = "sr.lelissiry@students.srvusd.net"
    password = "ID#166519"
else:
    password = input("Enter Google Account Password: ")

driver = webdriver.Chrome()
#try:
#    driver
#except ValueError:
#    print("Ensure that ChromDriver is in same folder as program.")

driver.get(GoogleSheet)

#Input Email
elem = driver.find_element_by_name('Email')
elem.send_keys(account)
elem.send_keys(Keys.RETURN)

time.sleep(.5)

#Input Password
elem = driver.find_element_by_name('Passwd')
elem.send_keys(password)
elem.send_keys(Keys.RETURN)


#----------------------------------------------------------------------
#       Initializing Google sheet
#----------------------------------------------------------------------

startrow = int(input("First Row: "))
while startrow < 2:
    print("ERROR: The first row must be a number greater than 1...")
    startrow = int(input("First Row: "))
endrow = int(input("Last Row: "))
while endrow <= startrow:
    print("ERROR: The end row must be a number greater than the start row...")
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

# For each row, complete all following code
for r in range(rnge):


#----------------------------------------------------------------------
#       Storing Google sheets data
#----------------------------------------------------------------------


# First Name
    elem = driver.find_element_by_class_name('cell-input')
    SheetsFirstName = elem.get_attribute('innerText')[:-1]
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

# Last Name
    elem = driver.find_element_by_class_name('cell-input')
    SheetsLastName = elem.get_attribute('innerText')[:-1]
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

# ID Number
    elem = driver.find_element_by_class_name('cell-input')
    SheetsID = elem.get_attribute('innerText')
    try:
        SheetsID = int(SheetsID)
    except ValueError:
        SheetsID = 0
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

# Grade Level
    elem = driver.find_element_by_class_name('cell-input')
    SheetsGrade = elem.get_attribute('innerText')
    try:
        SheetsGrade = int(SheetsGrade)
    except ValueError:
        SheetsGrade = 0
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    for v in range(5):
        actions.perform()

# Transcript Link
    elem = driver.find_element_by_class_name('cell-input')
    transcriptlink = elem.get_attribute('innerText')[:-1]
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    for v in range(3):
        actions.perform()

# Reason
    elem = driver.find_element_by_class_name('cell-input')
    SheetsReason = elem.get_attribute('innerText')[:-1]


#----------------------------------------------------------------------
#       Compares Google sheets input with transcript
#----------------------------------------------------------------------


# If doesn't have data, do not open link, skip to next row
    if SheetsFirstName + SheetsLastName == "":
        transcript = ""
        reason = ""

# If row is manually checked and has "*" in Reason Column, skip to next row
    elif "*" in SheetsReason:
        transcript = ""
        reason = ""

# If it does have data, open link
    else:
        driver.execute_script("window.open('" + transcriptlink + "', 'new_window')")
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(SleepTime)
# Set variables
        transcript = "NO"
        Classes = []
        reason = ""

# Open link
        elem = driver.find_elements_by_class_name('drive-viewer-paginated-page-reader-block')

# Look for specific element in transcript
        if elem != []:
# If the element exists, convert all text to string
            TranscriptText = []
            for i in range(len(elem)):
                text = elem[i]
                TranscriptText.append(text.get_attribute('innerText'))
                
# If link goes to transcript, find details
            if TranscriptText[0] == "Student Information":
                TranscriptLastName = TranscriptText[-5].split(",")[0]
                elem = TranscriptText[1]
                TranscriptID = int(elem.split(" ")[2])
                TranscriptGrade = int(elem.split(" ")[4])
                transcript = "YES"

# If link goes to report card, find details
            elif TranscriptText[0] == "GPA Summary:":
                reason = "Report Card"#TranscriptLastName = TranscriptText[-2].split(",")[0]

# If link goes to document with element, but not a transcript or report card
            else:
                reason = "Unknown document"
          
# If element doesn't exist, check if document isn't shared
        else:
            elem = driver.find_elements_by_id('requestButton')
            if elem != []:
                reason = "Need to request access"

# If link doesn't need to be shared, it is invalid
            else:
                reason = "Link doesn't work"
                
# If found valid document, make sure all details match
    if transcript == "YES":
        if TranscriptLastName == SheetsLastName:
            if TranscriptID == SheetsID:
                if TranscriptGrade == SheetsGrade:
                    if SheetsGrade == 9:
                        SheetsGrade = "09"
                    else:
                        SheetsGrade = str(SheetsGrade)
                    if (SchoolYear + " Grade " + SheetsGrade + " Term " + TermNum) in TranscriptText:
                        transcript = "YES"
                    else:
                        reason = "Outdated transcript"
                else:
                    reason = "Grade doesn't match"
            else:
                reason = "ID doesn't match"
        else:
            reason = "Name doesn't match"
            
    if reason != "":
        transcript = "NO"

            
#----------------------------------------------------------------------
#       Looks in transcript for classes and grades
#----------------------------------------------------------------------


# locates classes and grades for most recent term from TranscriptText and stores in Classes
    if transcript == "YES":
        start = 0
        end = 0
        for i in range(len(TranscriptText)):
            if TranscriptText[i] == SchoolYear + " Grade " + SheetsGrade + " Term " + TermNum \
               and start == 0:
                start = i
            if "Credit:" in TranscriptText[i] and start != 0 and end == 0:
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
                    if "." in CurrentTerm[i+n] and len(CurrentTerm[i+n-1]) == 1 \
                       and CurrentTerm[i+n-1] in ['A','B','C','D','F','P']:
                        Grade = CurrentTerm[i+n-1]
                        Classes.append(Grade)
                        n = -1


#----------------------------------------------------------------------
#       Checking Grades against CSF Requirements
#----------------------------------------------------------------------


# Converts grades to numbers
        for Class in range(0,len(Classes),2):
            Grade = Classes[Class + 1]
            if Grade ==  "A":
                Grade = 3
            elif Grade == "B":
                Grade = 1
            elif Grade == "C":
                Grade = 0
            else:
                Grade = -1
                transcript = "NO"
                reason = "D or F in a course"
            Classes[Class + 1] = Grade

# Adds points for A's & B's in honors & AP classes, up to 2 points
    if transcript == "YES":
        NumAPH = 0
        for List in [List1,List2,List3]:
            for Grade in [3,1]:
                for Class in range(0,len(Classes),2):
                    if NumAPH < 2 and Classes[Class] in List and Classes[Class + 1] == Grade and \
                        (Classes[Class][5] == "P" or Classes[Class][5] == "H"):
                        Classes[Class + 1] = Classes[Class + 1] + 1
                        NumAPH += 1
        ClassesLeft = Classes[:]
        NumClasses = 0
        NumPoints = 0

# Checks for List 1 requirements
# - at least 2 List I courses
# - at least 4 List I points
    if transcript == "YES":
        for Grade in range(4,-1,-1):
            for Class in range(len(ClassesLeft)-2,-1,-2):
                if ClassesLeft[Class] in List1 and \
                   ClassesLeft[Class + 1] == Grade and \
                   (NumPoints < 4 or NumClasses < 2) and NumClasses < 5:
                    NumClasses += 1
                    NumPoints += ClassesLeft[Class + 1]
                    del ClassesLeft[Class + 1]
                    del ClassesLeft[Class]
        if NumClasses < 2:
            transcript = "NO"
            reason = "< 2 List I courses"
        if NumPoints < 4:
            transcript = "NO"
            reason = "< 4 points from List I"

# Checks for List 2 requirements
# - at least 3 List 1 & 2 courses
# - at least 7 List 1 & 2 points
    if transcript == "YES":
        for Grade in range(4,-1,-1):
            for Class in range(len(ClassesLeft)-2,-1,-2):
                if (ClassesLeft[Class] in List1 or ClassesLeft[Class] in List2) and \
                   ClassesLeft[Class + 1] == Grade and \
                   (NumPoints < 7 or NumClasses < 3) and NumClasses < 5:
                    NumClasses += 1
                    NumPoints += ClassesLeft[Class + 1]
                    del ClassesLeft[Class + 1]
                    del ClassesLeft[Class]
        if NumClasses < 3:
            transcript = "NO"
            reason = "< 3 List I & II courses"
        if NumPoints < 7:
            transcript = "NO"
            reason = "< 7 points from List I & II"

# Checks for List 3 requirements
# - at most 5 courses
# - at least 10 List 1, 2, & 3 points
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
            reason = "< 10 points from List I - III"


#----------------------------------------------------------------------
#       Input transcript info and returning to next row
#----------------------------------------------------------------------


    if transcript != "":
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

        if SheetsReason != "Requested Access" or Classes != []:
            actions = ActionChains(driver)
            actions.send_keys(Keys.DELETE,Keys.ENTER)
            actions.perform()
            actions = ActionChains(driver)
            actions.send_keys(reason)
            actions.perform()
            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB)
        
        actions.send_keys(Keys.ARROW_LEFT)
        actions.perform()

        actions = ActionChains(driver)
        actions.send_keys(Keys.DELETE,Keys.ENTER)
        actions.perform()
        actions = ActionChains(driver)
        actions.send_keys(transcript)
        actions.perform()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_LEFT)
        for v in range(10):
            actions.perform()
            
    else:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_LEFT)
        for v in range(11):
            actions.perform()


#----------------------------------------------------------------------
#       Printing info for row
#----------------------------------------------------------------------


    print("\n","Row: ",startrow + r,sep="")
    if SheetsFirstName + SheetsLastName == "":
        print("NO PERSON!")
    else:
        print(SheetsFirstName,SheetsLastName)
        if "*" not in SheetsReason:
            if Classes != []:
                print(Classes)
            print("Transcript:",transcript)
        else:
            print("Transcript Manually Checked")
        if reason != "":
            print("Reason:",reason)
