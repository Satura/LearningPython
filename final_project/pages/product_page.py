import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project.base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # filter-form
    is_in_stock = '//input[@id="edit-stock-1"]'
    all_stock = '//input[@id="edit-stock-0"]'
    price_min = '//input[@id="edit-sell-price-min"]'
    price_max = '//input[@id="edit-sell-price-max-wrapper"]'
    filter_cats = '//div[@class="views-widget"]'
    filter_find_btn = '//input[@id="edit-submit-uc-products"]'
    filter_check_boxes = '//label[@class="option"]'
    filter_cat_brand = '/html/body/div[2]/div/div[4]/div[2]/div[1]/form/div/div/div/div[9]/div/fieldset/legend/a'
    filter_cat_cover = '/html/body/div[2]/div/div[4]/div[2]/div[1]/form/div/div/div/div[10]/div/fieldset/legend/a'
    filter_cat_paper_color = '/html/body/div[2]/div/div[4]/div[2]/div[1]/form/div/div/div/div[11]/div/fieldset/legend/a'
    filter_cat_cover_color = '/html/body/div[2]/div/div[4]/div[2]/div[1]/form/div/div/div/div[12]/div/fieldset/legend/a'
    filter_cat_usage = '/html/body/div[2]/div/div[4]/div[2]/div[1]/form/div/div/div/div[13]/div/fieldset/legend/a'
    # products-list
    view_90 = '//li[@class="pager-item"]'
    open_menu_add_to_cart_btns = '//span[@class="show-addcart"]'
    add_to_cart_btn = '//input[@class="form-submit node-add-to-cart ajax-cart-submit-form-button ajax-cart-processed"]'
    cart_btn = "//span[@class='head-cart-title']"

    def get_all_filters(self):
        return self.driver.find_elements(By.XPATH, self.filter_cats)

    def get_filter_btn(self):
        return self.driver.find_element(By.XPATH, self.filter_find_btn)

    def get_all_checkboxes(self):
        return self.driver.find_elements(By.XPATH, self.filter_check_boxes)

    def get_radio_in_stock(self):
        return self.driver.find_element(By.XPATH, self.is_in_stock)

    def get_all_alltocarts_btns(self):
        return self.driver.find_elements(By.XPATH, self.open_menu_add_to_cart_btns)

    def get_addtocard_real_btn(self):
        return self.driver.find_element(By.XPATH, self.add_to_cart_btn)

    def get_count_in_cart(self):
        count = int(self.driver.find_element(By.XPATH, self.count_in_cart).text.split()[1])
        return count

    # actions
    def open_all_filters(self):
        self.driver.find_element(By.XPATH, self.filter_cat_usage).click()
        self.driver.find_element(By.XPATH, self.filter_cat_cover_color).click()
        self.driver.find_element(By.XPATH, self.filter_cat_paper_color).click()
        self.driver.find_element(By.XPATH, self.filter_cat_cover).click()
        self.driver.find_element(By.XPATH, self.filter_cat_brand).click()

    def choose_only_in_stock(self):
        self.get_radio_in_stock().click()

    def click_find_filter_btn(self):
        self.get_filter_btn().click()

    def choose_prod_to_add_to_cart(self, i):
        self.get_all_alltocarts_btns()[i].click()
        time.sleep(1)
        self.get_addtocard_real_btn().click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_btn))).click()
