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


transcript = "NO"
reason = ""

LastName = "Column E"
ID = int("Column F")
Grade = int("Column G")

TranscriptLastName = "Michaud"

stringNumID = "Student Number: 166762 Grade: 12"
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
