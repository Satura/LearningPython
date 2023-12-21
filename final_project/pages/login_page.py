from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project.base.base_class import Base
from final_project.pages.home_page import Home_page
from final_project.utilities.logger import Logger


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    login_field = "//input[@id='edit-name']"
    pass_field = "//input[@id='edit-pass']"
    login_btn = "//input[@id='edit-submit']"

    # getters
    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_pass_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pass_field)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    # actions
    def input_login(self, login):
        self.get_login_field().send_keys(login)
        print('input login')

    def input_password(self, password):
        self.get_pass_field().send_keys(password)
        print('input password')

    def login_click(self):
        self.get_login_btn().click()
        print('click login btn')

    def authorization(self):
        # hp = Home_page(self.driver)
        # hp.open_site()
        # hp.go_to_auth()
        Logger().add_start_step(method="authorization")
        self.input_login(Base.INDILOGIN)
        self.input_password(Base.INDIPASS)
        self.login_click()
        Logger.add_end_step(url=self.driver.current_url, method="authorization")
