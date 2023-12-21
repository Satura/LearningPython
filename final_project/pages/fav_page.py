import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project.base.base_class import Base
from final_project.utilities.logger import Logger


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
        count = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_in_cart))).text.split()[1]
        return count

    def add_to_cart_all_fav(self):
        Logger().add_start_step(method="add_to_cart_all_fav")
        for e in self.get_prods_to_shop():
            e.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.products_addcart_btn).click()
        Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_all_fav")



