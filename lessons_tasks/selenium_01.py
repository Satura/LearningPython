from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform

driver_path = ''
if platform == 'linux':
    driver_path = '../webdriver/geckodriver'
elif platform == 'win32':
    driver_path = '../webdriver/geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))
base_url = 'https://saucedemo.com'

# авторизация
driver.get(base_url)

username = 'standard_user'
password = 'secret_sauce'

un_field = driver.find_element(by=By.XPATH, value='//*[@id="user-name"]')
un_field.send_keys(username)
pw_field = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
pw_field.send_keys(password)
login_btn = driver.find_element(by=By.ID, value='login-button')
login_btn.click()
print('Авторизовались, ура. ')

# получение сведений о товарах
product_cards = driver.find_elements(by=By.CLASS_NAME, value='inventory_item')
product_names = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
product_prices = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_price')
product_btns = driver.find_elements(by=By.CLASS_NAME, value='btn_inventory')
sum = 0

# добавление первых двух единиц в корзину
for i in range(2):
    print(f'Продукт # {i + 1} . Название: {product_names[i].text}, цена: {product_prices[i].text}')
    sum += float(product_prices[i].text.replace('$', ''))
    product_btns[i].click()
print(sum)
# save item's names and prices
product_1_name = product_names[0].text
product_2_name = product_names[1].text
product_1_price = product_prices[0].text
product_2_price = product_prices[1].text

# переход в корзину, получение сведений о товарах в корзине
shopping_container = driver.find_element(by=By.ID, value='shopping_cart_container')
shopping_container.click()

items = driver.find_elements(by=By.CLASS_NAME, value='cart_item')
item_names = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
item_prices = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_price')
sum_in_shoppnig = 0
for i in range(2):
    print(f'Продукт в корзине # {i + 1}. Название: {item_names[i].text}, цена: {item_prices[i].text}')
    sum_in_shoppnig += float(item_prices[i].text.replace('$', ''))
print(sum_in_shoppnig)

# оформление покупки
checkout_btn = driver.find_element(by=By.ID, value='checkout')
checkout_btn.click()

first_name_field = driver.find_element(by=By.ID, value='first-name')
last_name_field = driver.find_element(by=By.ID, value='last-name')
zip_code_name_field = driver.find_element(by=By.ID, value='postal-code')

first_name_field.send_keys('Maria')
last_name_field.send_keys('Vorlich')
zip_code_name_field.send_keys(987546)

continue_btn = driver.find_element(by=By.ID, value='continue')
continue_btn.click()

# информация из чека
finish_items = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
finish_prices = driver.find_elements(by=By.CLASS_NAME, value='inventory_item_price')
finish_sum = driver.find_element(by=By.CLASS_NAME, value='summary_subtotal_label')  # сумма в чеке до налога
total_sum = 0  # сумма до налога, которая должна быть
for i in range(2):
    print(f'Куплен продукт # {i + 1}. Название: {finish_items[i].text}, цена: {finish_prices[i].text}')
    total_sum += float(finish_prices[i].text.replace('$', ''))
print(finish_sum)

# проверки
try:
    assert float(finish_sum.text.replace('Item total: $', '')) == total_sum
    print('Суммы заказа и чека совапали')
except AssertionError:
    print('Суммы заказа и чека не совапали')

try:
    assert finish_items[0].text == product_1_name
    assert finish_items[1].text == product_2_name
    print('Наименования заказанных товаров и чека совпали')
except AssertionError:
    print('Наименования заказанных товаров и чека не совпали')

try:
    assert finish_prices[0].text == product_1_price
    assert finish_prices[1].text == product_2_price
    print('Цены заказанных товаров и чека совпали')
except AssertionError:
    print('Цены заказанных товаров и чека не совпали')

driver.close()
