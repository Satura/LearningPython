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
    name_field = '//input[@id="edit-panes-fioDelivery-fio-name"]'
    phone_field = '//input[@id="edit-panes-phoneDelivery-phone"]'
    promo_field = '//input[@id="edit-panes-uc-discounts-coupon-code"]'
    comment_field = '//input[@id="edit-panes-comments-comments"]'
    pickup_radio = '//input[@value="flatrate_7308---0"]'
    runner_radio = '//input[@value="flatrate_42---0"]'
    address_field = '//input[@id="edit-panes-addressDelivery-street"]'
    robokassa_radio = '//label[@for="edit-panes-payment-payment-method-robokassa"]'


    # getters
