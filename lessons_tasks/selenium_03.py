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

# приветствие, вывод предложений и получение ответа покупателя
print('Приветствую тебя в нашем интернет магазине')
print('Выбери один из следующих товаров и укажи его номер:')
for i in range(len(product_cards)):
    print(f'{i + 1} - {product_names[i].text}')

while True:
    try:
        chosen = int(input('желаемый номер - '))
        break
    except ValueError:
        print('введен не номер, попробуй ее раз')
        continue

while True:
    if chosen < 1 or chosen > len(product_cards):
        chosen = int(input('не правильно указан номер, выбери другой - '))
    else:
        break

ch_prod_name = product_names[chosen - 1].text
ch_prod_price = float(product_prices[chosen - 1].text.replace('$', ''))
print(f'{ch_prod_name} за ${ch_prod_price}, отличный выбор')

# добавление товара в корзину и переход в корзину
product_btns[chosen - 1].click()

shopping_container = driver.find_element(by=By.ID, value='shopping_cart_container')
shopping_container.click()

items = driver.find_elements(by=By.CLASS_NAME, value='cart_item')
item_name = driver.find_element(by=By.CLASS_NAME, value='inventory_item_name')
item_price = driver.find_element(by=By.CLASS_NAME, value='inventory_item_price')

try:
    assert item_name.text == ch_prod_name
    assert float(item_price.text.replace('$', '')) == ch_prod_price
    print('В корзину попало то, что нужно')
except AssertionError:
    print('упс, не тот товар или цена')

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
finish_item = driver.find_element(by=By.CLASS_NAME, value='inventory_item_name')
finish_price = driver.find_element(by=By.CLASS_NAME, value='inventory_item_price')
finish_sum = driver.find_element(by=By.CLASS_NAME, value='summary_subtotal_label')  # сумма в чеке до налога

try:
    assert finish_item.text == ch_prod_name
except AssertionError:
    print('Название не совпало')

try:
    assert float(finish_price.text.replace('$', '')) == ch_prod_price
except AssertionError:
    print('Цена не совпала')

try:
    assert float(finish_sum.text.replace('Item total: $', '')) == ch_prod_price
except AssertionError:
    print('Итоговая сумма (до налогов) не совпала')
print('На оформлении правильный товар')

finish_btn = driver.find_element(by=By.ID, value='finish')
finish_btn.click()
complete_header = driver.find_element(by=By.CLASS_NAME, value='complete-header')
print(complete_header.text)
