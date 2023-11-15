from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
from selenium_04.inventory_page import Inventory_Page
from selenium_04.login_page import Login_Page

# Определяем где взять webdriver в зависимости от используемой ОС
driver_path = ''
if platform == 'linux':
    driver_path = '.././webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '.././webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))

# Открываем страницу тестируемого сервиса и получаем логины
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
password = 'secret_sauce'
uns = driver.find_element(By.ID, 'login_credentials')
usernames = uns.text.split('\n')
usernames.remove('Accepted usernames are:')
login_pg = Login_Page(driver)
inv_pg = Inventory_Page(driver)

# Поочередно для каждого пользователя тестируем авторизацию на сайте
for u in usernames:
    try:
        login_pg.authorization(u, password)
        expect_page = 'https://www.saucedemo.com/inventory.html'
        actual_page = driver.current_url
        assert expect_page == actual_page
        print('Успешная авторизация вот этим пользователем:', u)
    except AssertionError:
        try:
            print('Не смогли авторизоваться')
            locked_user_message = 'Epic sadface: Sorry, this user has been locked out.'
            assert login_pg.get_error_message() == locked_user_message
            print('Попытка авторизоваться заблокированным пользователем:', u)
            driver.refresh()
        except AssertionError as ae:
            print('Что-то пошло не так', ae)
    else:
        inv_pg.logout()
        assert driver.current_url == base_url
        print("Успешно разлогинились")

driver.close()

# Первый тест, успешная авторизация
# print('First test - Success authorization')
# login_pg.authorization(username, password)
# expect_page = 'https://www.saucedemo.com/inventory.html'
# actual_page = driver.current_url
# assert expect_page == actual_page
# print("Success authorization")
#
# inv_pg.logout()
# assert driver.current_url == base_url
# print("Success logedout")

# Второй тест, попытка зайти заблокированным пользователем
# print('Second test - Locked user authorization')
# locked_user_message = 'Epic sadface: Sorry, this user has been locked out.'
# login_pg.authorization(locked_user, password)
# assert login_pg.get_error_message() == locked_user_message
# print('Successfully locked user was not allowed in')
# driver.refresh()

# Третий тест, авторизация проблемным пользователем (в каталоге все картинки одинаковые)
# print('Second test - Problem user authorization')
# login_pg.authorization(problem_user, password)
# expect_page = 'https://www.saucedemo.com/inventory.html'
# actual_page = driver.current_url
# assert expect_page == actual_page
# print("Success authorization")
#
# product_imgs = inv_pg.get_items_imgs()
# imgs_urls = [product_imgs[i].get_attribute('src') for i in range(1, len(product_imgs), 2)]
# for i in range(len(imgs_urls)-1):
#     assert imgs_urls[i] == imgs_urls[i+1]
# print('all images are equals')
#
# inv_pg.logout()
# assert driver.current_url == base_url
# print("Success logedout")
