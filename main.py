import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
 
driver_path = ''
if platform == 'linux':
    driver_path = './webdriver/geckodriver'
elif platform == 'win32':
    driver_path = './webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))

driver.get('https://saucedemo.com')
time.sleep(5)
driver.close()

# user_name = driver.find_element(by=By.ID, value='user-name')
# user_name.send_keys('standard_user')
# password = driver.find_element(by=By.NAME, value='password')
# password.send_keys('secret_sauce')
# login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login-button"]')
# login_btn.click() 

