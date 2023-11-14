from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Login_Page:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login, password):
        username_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        login_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))

        username_field.send_keys(login)
        password_field.send_keys(password)
        login_btn.click()

    def get_error_message(self):
        locked_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="error-message-container error"]')))
        return locked_field.text

    def close_error_message(self):
        close_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="error-button"]')))
