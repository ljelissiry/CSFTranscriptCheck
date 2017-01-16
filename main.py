import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

nlocation = "/Users/nolanbonnie/Desktop/Python/chromedriver"
elocation =
llocation = 

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
startrow = int(input("What row do you want to start on?"))
endrow = int(input("What row do you want to end on?"))
rnge = endrow - startrow

#String text = driver.findElement(By.id("some id")).getText()

for i in range(rnge):
    scroll = startrow - 1 + i
    for v in range(scroll):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
    for v in range(5):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    actions = ActionChains(driver)
    actions.key_down(Keys.COMMAND)
    actions.send_keys("C")
    actions.key_up(Keys.COMMAND)
    actions.perform()
    
        
    transcript = "NO"
    reason = ""

    SheetsLastName = "Column E"
    SheetsID = int("Column F")
    SheetsGrade = int("Column G")

    TranscriptLastName = "Michaud"

    TranscriptStringNumID = "Student Number: 166762 Grade: 12"
    TranscriptID = int(stringNumID.split(" ")[2])
    TranscriptGrade = int(stringNumID.split(" ")[4])

    if LastName == TranscriptLastName:
        if TranscriptID == ID:
            if TranscriptGrade == Grade:
                transcript = "YES"
            else:
                reason = "Grade does not match"
        else:
            reason = "ID does not match"
    else:
        reason = "Name does not match"
