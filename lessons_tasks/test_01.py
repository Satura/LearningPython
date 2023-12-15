import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
 
base_url = 'https://saucedemo.com'
login = 'standard_user'
password_common = 'secret_sauce'

driver_path = ''
if platform == 'linux':
    driver_path = '../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))
    
driver.get(base_url)

user_name = driver.find_element(by=By.ID, value='user-name')
user_name.send_keys(login)
password = driver.find_element(by=By.NAME, value='password')
password.send_keys(password_common)
login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login-button"]')
login_btn.click() 

text_pr = driver.find_element(by=By.CLASS_NAME, value='title')
value_text = text_pr.text
try:
    assert value_text == 'Products'
except AssertionError: 
    print('We have an assertion error 1')
else:
    print('All is fine 1')

current_url = driver.current_url
expected_url = 'https://www.saucedemo.com/inventory.html'

try:
    assert current_url == expected_url
except AssertionError: 
    print('We have an assertion error 2')
else:
    print('All is fine 2')

driver.close()