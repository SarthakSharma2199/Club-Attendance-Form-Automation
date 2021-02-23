import pandas as pd
from selenium import webdriver
import time

participants=pd.read_excel("./participants.xlsx")
print(participants)

web=webdriver.Chrome("./chromedriver.exe")

web.get('https://docs.google.com/forms/d/e/1FAIpQLSfJ9cOpTOMpJhm_3pia04ocgGCEE70RyEEoYjOSgEtMt5O9qg/viewform')
# web.implicitly_wait(5)
time.sleep(1)

club_email="demo@gmail.com"
club_or_chapter="Club"
club_or_chapter_name="Dance Club"

form_email=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
form_email.send_keys(club_email)

club_or_chapter_dropdown=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
club_or_chapter_dropdown.click()
time.sleep(1)
club_or_chapter_option = web.find_elements_by_xpath("//div//span[contains(., 'Club')]")
for i in club_or_chapter_option:
    try:
        i.click()
    except Exception as e:
        print(e)

club_or_chapter_name_dropdown=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
club_or_chapter_name_dropdown.click()
time.sleep(1)
club_or_chapter_name_option = web.find_elements_by_xpath("//div//span[contains(., 'Dance club')]")
for i in club_or_chapter_name_option:
    try:
        i.click()
    except Exception as e:
        print(e)

