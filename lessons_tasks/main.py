import os
import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from sys import platform
from selenium.webdriver.common.keys import Keys


driver_path = ''
if platform == 'linux':
    driver_path = '../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))

# driver.get('https://saucedemo.com')
# time.sleep(5)
#
# user_name = driver.find_element(by=By.ID, value='user-name')
# user_name.send_keys('standard_user')
# password = driver.find_element(by=By.NAME, value='password')
# password.send_keys('secret_sauce')
# login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login-button"]')
# login_btn.click()
#
# driver.close()

driver.get('https://indinotes.com')
print('Website is opened')
enter_link = driver.find_element(By.XPATH, "//a[@href='/user?destination=node']")
enter_link.click()
print('Login page is opened')
login_field = driver.find_element(By.XPATH, "//input[@id='edit-name']")
pass_field = driver.find_element(By.XPATH, "//input[@id='edit-pass']")
login_field.send_keys(os.environ['INDILOGIN'])
pass_field.send_keys(os.environ['INDIPASS'])
login_btn = driver.find_element(By.XPATH, "//input[@id='edit-submit']")
login_btn.click()
print('Authorization is success')

