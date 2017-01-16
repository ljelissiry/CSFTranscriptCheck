import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

nlocation = "/Users/nolanbonnie/Desktop/Python/chromedriver"
elocation = ""
llocation = ""

loc = input("Who is using the code?")
if loc == "nolan":
    driver = webdriver.Chrome(nlocation)
elif loc == "eric":
    driver = webdriver.Chrome(elocation)
elif loc == "luke":
    driver = webdriver.Chrome(llocation)
else:
    print("input not recognized")
    
driver.get("https://docs.google.com/spreadsheets/d/1ch5pT5ywKXvINhlhDJzvdl0YgxRjSdHKPzIf-ht5qgw/edit#gid=1082589385")

#Input Email--------------------------------------------------
email = input("Email:   ")
elem = driver.find_element_by_name('Email')
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
#Input Password--------------------------------------------------
passw = input("Password:    ")
elem = driver.find_element_by_name('Passwd')
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)

startrow = int(input("What row do you want to start on?"))
endrow = int(input("What row do you want to end on?"))
rnge = endrow - startrow
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
    SheetsLastName = elem.get_attribute('innerText')
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

       #Transcript
    elem = driver.find_element_by_class_name('drive-viewer-paginated-page-reader-block')
    TranscriptStringNumID = elem.get_attribute('innerText')
    #TranscriptStringNumID = "Student Number: 166762 Grade: 12"
    TranscriptID = int(TranscriptStringNumID.split(" ")[2])
    TranscriptGrade = int(TranscriptStringNumID.split(" ")[4])
    elem = driver.find_element_by_class_name('drive-viewer-paginated-page-reader-block')
    TranscriptNameString = "Elissiry, Luke Jacques"
    TranscriptLastname = TranscriptNameString.split(" ")[1]

    if SheetsLastName == TranscriptLastName:
        if SheetsID == TranscriptID:
            if SheetsGrade == TranscriptGrade:
                transcript = "YES"
            else:
                reason = "Grade does not match"
        else:
            reason = "ID does not match"
    else:
        reason = "Name does not match"
