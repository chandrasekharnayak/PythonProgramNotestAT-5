from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://treenetra.in/')

time.sleep(20)

driver.quit()






