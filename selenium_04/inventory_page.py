from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

class Inventory_Page:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        menu_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        menu_btn.click()
        logout_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout_btn.click()

    def get_items_imgs(self):
        imgs = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_img')
        return imgs
