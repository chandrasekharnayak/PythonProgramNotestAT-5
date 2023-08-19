from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')

driver= webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/client')

forget_text = driver.find_element(By.LINK_TEXT,'Forgot password?')
forget_text.click()
time.sleep(3)
register_partial_link_test = driver.find_element(By.PARTIAL_LINK_TEXT,'Reg')
register_partial_link_test.click()

first_name = driver.find_element(By.CLASS_NAME,'form-control').send_keys('Chandra')
last_name = driver.find_element(By.ID,'lastName').send_keys('Nayak')

email =  driver.find_element(By.ID,'userEmail').send_keys('k.csnayak108@gmail.com')
phone_number =  driver.find_element(By.ID,'userMobile').send_keys('8895139108')

#Selective Drop Down

occupation_drop_down = Select(driver.find_element(By.CLASS_NAME,'custom-select'))
# occupation_drop_down.select_by_visible_text('Engineer')
occupation_drop_down.select_by_index(3)


user_password = driver.find_element(By.ID,'userPassword').send_keys('Qwerty@108^^')
confirm_user_password = driver.find_element(By.ID,'confirmPassword').send_keys('Qwerty@108^^')

check_box = driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

time.sleep(10)
register = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
driver.quit()
