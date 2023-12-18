import datetime
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from final_project.pages.login_page import Login_page
from final_project.pages.home_page import Home_page
from final_project.pages.fav_page import Fav_page
from final_project.pages.product_page import Product_page
from final_project.pages.cart_page import Cart_page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '.././webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '.././webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))
now_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
name_scrsh = 'screenshot_' + now_date + '.png'
def test_shop_fav():
    print('Авторизация...')
    hp = Home_page(driver)
    lp = Login_page(driver)
    hp.open_site()
    hp.go_to_auth()
    lp.authorization()
    assert driver.find_element(By.XPATH, hp.profile_link).is_displayed()
    print('Успешно авторизовались, переходим в Избранное')

    hp.go_to_favorite()
    fp = Fav_page(driver)
    assert driver.current_url == 'https://indinotes.com/favorites'
    print('Избранное открыто')

    print('Добавление в корзину всего избранного')
    fp.add_to_cart_all_fav()
    time.sleep(2)
    print('В корзине товаров: ', fp.get_count_in_cart())
    assert int(fp.get_count_in_cart()) == len(fp.get_prods_to_shop())


def test_find_add_new():
    print('Переходим к новинкам')
    hp = Home_page(driver)
    hp.go_to_new()
    pp = Product_page(driver)
    assert driver.current_url == 'https://indinotes.com/novelty'
    print('Новинки открыты')

    print('Раскрыть все филтры')
    pp.open_all_filters()
    print('Выбрать фильтры: в наличии, точка, BRAUBERG, Falafel books, Leuchtturm1917')
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

    driver.save_screenshot('./screen/' + name_scrsh)

    if len(pp.get_all_alltocarts_btns()) != 0:
        pp.choose_prod_to_add_to_cart(0)
        print('Первый попавшийся товар добавлен')

    else:
        print('Нет ничего по этим фильтрам')

    print('Сформировали корзину, переходим к ней')

def test_clear_cart():
    hp = Home_page(driver)
    hp.go_to_cart()
    assert driver.current_url == 'https://indinotes.com/cart'
    print('Зашли в корзину, всплакнули от суммы и все удаляем')

    driver.save_screenshot('./screen/' + name_scrsh)

    cp = Cart_page(driver)
    cp.clear_cart()
    assert cp.get_isempty_cart()  # == "Корзина\nКорзина пуста"
    print('Корзина пуста')
    driver.save_screenshot('./screen/' + name_scrsh)

    driver.close()
