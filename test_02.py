from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
 
driver_path = ''
if platform == 'linux':
    driver_path = './webdriver/geckodriver'
elif platform == 'win32':
    driver_path = './webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))

base_url = 'https://saucedemo.com'

# негативная проверка (неправильный логин и/или пароль)
username = '231321321'
password = '321232132'

driver.get(base_url)
username_field = driver.find_element(by=By.ID, value='user-name')
username_field.send_keys(username)
password_field = driver.find_element(by=By.NAME, value='password')
password_field.send_keys(password)
login_btn = driver.find_element(by=By.XPATH, value='//*[@id="login-button"]') 
login_btn.click() 
error_block = driver.find_element(by=By.CSS_SELECTOR, value='.error-message-container > h3:nth-child(1)')

error_message = error_block.text
wrong_params_message = 'Epic sadface: Username and password do not match any user in this service'
empty_params_message = 'Epic sadface: Username is required'

try:
    assert error_message == wrong_params_message
except AssertionError: 
    print('We have an assertion error. Wrong params message don\'t work')
else:
    print('All is fine. Wrong params message works')

# негативная проверка (пустые поля логина и/или пароля)
username_field.clear()
password_field.clear()
login_btn.click() 
error_message = error_block.text
try:
    assert error_message == empty_params_message
except AssertionError: 
    print('We have an assertion error. Empty params message don\'t work')
else:
    print('All is fine. Empty params message works')

driver.close()
   