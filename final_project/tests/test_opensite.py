from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from lessons_tasks.selenium_04.inventory_page import Inventory_Page
from final_project.pages.login_page import Login_page
from final_project.pages.home_page import Home_page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '../../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))


def test_open_site():
    print('Start open test')
    hp = Home_page(driver)
    hp.open_site()
    assert driver.current_url == 'https://indinotes.com/'
    print('Open site pass')
    driver.close()


