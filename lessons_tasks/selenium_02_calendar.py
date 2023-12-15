import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sys import platform

driver_path = ''
if platform == 'linux':
    driver_path = '../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))
base_url = 'https://demoqa.com/date-picker'

driver.get(base_url)

# find date field
date_field = driver.find_element(by=By.ID, value="datePickerMonthYearInput")

# get current date & add 10 days
now_date = datetime.datetime.now()
new_date = now_date + datetime.timedelta(days=10)
print(now_date, "\n", new_date)

# input new date to field
date_to_send = new_date.strftime("%m/%d/%Y")
print(date_to_send)
date_field.clear()
time.sleep(3)
date_field.send_keys(date_to_send)
date_field.send_keys(Keys.RETURN)
