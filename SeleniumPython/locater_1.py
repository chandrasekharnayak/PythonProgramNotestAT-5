'''
Locater:-
8 locater extis in selenium

ID, NAME, CLASS NAME, TAG NAME
LINK TEXT, PARTIAL LINK TEXT
CSS SELECTOR , XPATH
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.facebook.com/login/')

email = driver.find_element(By.ID,'email')
email.send_keys('')

password = driver.find_element(By.ID,'pass')
password.send_keys('')

login_button = driver.find_element(By.ID,'loginbutton')
login_button.click()


time.sleep(10)
driver.quit()



