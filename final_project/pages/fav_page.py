import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project.base.base_class import Base

class Fav_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # products_list = '//div[@class="cat-title"]'
    # products_price_list = '//div[@class="uc-price-box"]'
    products_addcart_btn1_list = '//span[@class="show-addcart"]' # открывает окошко с выбором цвета и количества и дбавлением в корзину
    products_addcart_btn = '//input[@value="В корзину"]' # кнопка собственно добавления в корзину, у каждого продукта своя
    count_in_cart = '//a[@class="head-cart-link"]'

    def get_prods_to_shop(self):
        return self.driver.find_elements(By.XPATH, self.products_addcart_btn1_list)

    def get_count_in_cart(self):
        count = self.driver.find_element(By.XPATH, self.count_in_cart).text.split()[1]
        return count

    def add_to_cart_1_fav(self):
        self.get_prods_to_shop()[0].click()
        self.driver.find_element(By.XPATH, self.products_addcart_btn).click()

    def add_to_cart_all_fav(self):
        for e in self.get_prods_to_shop():
            e.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.products_addcart_btn).click()



