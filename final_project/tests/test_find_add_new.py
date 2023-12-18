import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from lessons_tasks.selenium_04.inventory_page import Inventory_Page
from final_project.pages.login_page import Login_page
from final_project.pages.home_page import Home_page
from final_project.pages.product_page import Product_page
from final_project.pages.cart_page import Cart_page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '../../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))


def test_find_add_new():
    print('Start login')
    hp = Home_page(driver)
    lp = Login_page(driver)
    hp.open_site()
    hp.go_to_auth()
    lp.authorization()
    assert driver.find_element(By.XPATH, hp.profile_link).is_displayed()
    print('Login success, go to Novelty')

    hp.go_to_new()
    pp = Product_page(driver)
    assert driver.current_url == 'https://indinotes.com/novelty'
    print('Новинки открыты')

    print('Раскрыть все филтры')
    pp.open_all_filters()
    print('Выбрать фильтры: в наличии, точка, Falafel books, Leuchtturm1917')
    for ch in pp.get_all_checkboxes():
        if ch.text == 'Точка':
            ch.click()
        if ch.text == 'BRAUBERG':
            ch.click()
        if ch.text == 'Falafel books':
            ch.click()
        if ch.text == 'Leuchtturm1917':
            ch.click()

    pp.click_find_filter_btn()
    if len(pp.get_all_alltocarts_btns()) != 0:
        pp.choose_prod_to_add_to_cart(0)
        print('Первый попавшийся товар добавлен')

    else:
        print('Нет ничего по этим фильтрам')


    driver.close()




