import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from lessons_tasks.selenium_04.inventory_page import Inventory_Page
from final_project.pages.login_page import Login_page
from final_project.pages.home_page import Home_page
from final_project.pages.fav_page import Fav_page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '../../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))


def test_shop_fav():
    print('Start login')
    hp = Home_page(driver)
    lp = Login_page(driver)
    hp.open_site()
    hp.go_to_auth()
    lp.authorization()
    assert driver.find_element(By.XPATH, hp.profile_link).is_displayed()
    print('Login success, go to Favorite')

    hp.go_to_favorite()
    fp = Fav_page(driver)
    assert driver.current_url == 'https://indinotes.com/favorites'
    print('Favorite is opened')

    # fp.add_to_cart_1_fav() # не умеет добавлять из этого же окошка, даже есть ввести другое количество
    print('Добавление в корзину всего избранного')
    fp.add_to_cart_all_fav()
    time.sleep(2)
    print('In cart is: ', fp.get_count_in_cart())
    assert int(fp.get_count_in_cart()) == len(fp.get_prods_to_shop())

    driver.close()




