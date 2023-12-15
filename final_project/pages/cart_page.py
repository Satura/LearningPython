import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project.base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    remove_btn_list = '//input[@title="Удалить"]'
    remove_first_el = '//input[@id="edit-items-0-remove"]'
    prices = '//td[@class="price price-one"]'
    qty_list = '//input[@class="form-text required ajax-cart-processed"]'
    sums_list = '//td[@class="price"]'
    refresh_cart_btn = '//input[@id="edit-update"]'
    order_btn = '//input[@id="edit-checkout"]'
    final_sum = '//td[@class="subprice"]' # обе с одинаковыми идентификаторами, получать список и выбирать 0ой элемент
    empty_cart_desc = '//span[@id="cart-block-contents-ajax"]'

    # getters
    def get_remove_btn_list(self):
        return self.driver.find_elements(By.XPATH, self.remove_btn_list)

    def get_remove_first_el(self):
        return self.driver.find_element(By.XPATH, self.remove_first_el)
    def get_prices_for_one_list(self):
        return self.driver.find_elements(By.XPATH, self.prices)

    def get_quantity_list(self):
        return self.driver.find_elements(By.XPATH, self.qty_list)

    def get_sums_list(self):
        return self.driver.find_elements(By.XPATH, self.sums_list)

    def get_refresh_cart_btn(self):
        return self.driver.find_element(By.XPATH, self.refresh_cart_btn)

    def get_form_order_btn(self):
        return self.driver.find_element(By.XPATH, self.order_btn)

    def get_final_sum_without_promo(self):
        return self.driver.find_elements(By.XPATH, self.final_sum)[0]

    def get_isempty_cart(self):
        return self.driver.find_element(By.XPATH, self.empty_cart_desc).text
    # actions
    def clear_cart(self):
        for i in range(len(self.get_remove_btn_list())):
            self.get_remove_first_el().click()
            time.sleep(1)