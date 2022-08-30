from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import pyautogui as p


spammer_mail = "Insert Here"
spammer_pass = "Insert Here"
reciever_mail = "Insert Here"
reciever_service = "gmail.com"
subject = "Insert Here"
content = "Insert Here"

driver = webdriver.Chrome(executable_path="chromedriver.exe")

             
driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(spammer_mail)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(spammer_pass)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(3)
driver.get("https://mail.google.com")
sleep(3)
for i in range(100):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(3)
    #CHANGE THIS PART UNDERNEATH
    p.typewrite(reciever_mail)
    p.hotkey('altright','q')
    p.typewrite(reciever_service)
    sleep(3)
    p.press("tab")
    p.press("tab")
    p.typewrite(subject)
    p.press("tab")
    p.typewrite(content)
    sleep(3)    
    p.click(555,929)
    sleep(3)
    
    


