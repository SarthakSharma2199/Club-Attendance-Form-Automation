import pandas as pd
from selenium import webdriver
import time

participants=pd.read_excel("./participants.xlsx")
print(participants)

web=webdriver.Chrome("./chromedriver.exe")

web.get('https://docs.google.com/forms/d/e/1FAIpQLSckKFDYqXQ9MeN-1YkfwiHEUgswCnpwCggOixFDX38cUxrCSA/viewform')
# web.implicitly_wait(5)
time.sleep(1)

club_email="demo@gmail.com"
club_or_chapter="Club"
club_or_chapter_name="Dance Club"

form_email=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
form_email.send_keys(club_email)