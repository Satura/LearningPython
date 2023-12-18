import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from lessons_tasks.selenium_04.inventory_page import Inventory_Page
from final_project.pages.login_page import Login_page
from final_project.pages.home_page import Home_page
from final_project.pages.cart_page import Cart_page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '../../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))


def test_clear_cart():
    print('Start login')
    hp = Home_page(driver)
    lp = Login_page(driver)
    hp.open_site()
    hp.go_to_auth()
    lp.authorization()
    assert driver.find_element(By.XPATH, hp.profile_link).is_displayed()
    print('Login success, go to Cart')

    hp.go_to_cart()
    assert driver.current_url == 'https://indinotes.com/cart'
    print('Cool! We are at cart')
    cp = Cart_page(driver)
    cp.clear_cart()
    assert cp.get_isempty_cart() # == "Корзина\nКорзина пуста"
    print('Cart is empty')

    driver.close()