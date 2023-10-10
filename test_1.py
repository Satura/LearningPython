import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
base_url = 'https://saucedemo.com'
login = 'standard_user'
password_common = 'secret_sauce'

driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path='./webdriver/geckodriver'))
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
    assert value_text == 'Produts'
except AssertionError: 
    print('We have an assertion error')
else:
    print('All is fine')
driver.close()