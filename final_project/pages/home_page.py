import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from final_project.base.base_class import Base


class Home_page(Base):
    home_url = 'https://indinotes.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    enter_link = "//a[@href='/user?destination=node']"
    profile_link = "//li[@class='user-profile']"
    logout_link = "//li[@class='user-logout']"
    fav_btn = "//a[@title='Избранные товары']"
    cart_btn = "//span[@class='head-cart-title']"
    new_btn = "//a[@href='/novelty']"  # новинки
    albums_btn = "//a[@href='/albumy']"  # скетчбуки и альбомы
    pocketbooks_btn = "//a[@href='/pocketbooks']"  # записные книжки
    notepads_btn = "//a[@href='/notepads']"  # блокноты
    planners_btn = "//a[@href='/planners']"  # ежедневники
    books_btn = "//a[@href='/knigi']"  # книги
    accessories_btn = "//a[@href='/accessories']"  # аксессуары
    actions_btn = "//a[@href='/actions']"  # акции
    brands_btn = "//a[@href='/brands']"  # бренды
    search_field = "//input[@name='keywords']"

    def open_site(self):
        with allure.step('Открытие сайта'):
            self.driver.get(self.home_url)

    def go_to_auth(self):
        with allure.step('Переход на страницу авторизации'):
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_link))).click()

    def go_to_favorite(self):
        with allure.step('Переход на страницу Избранного'):
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fav_btn))).click()

    def go_to_cart(self):
        with allure.step('Переход в корзину'):
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_btn))).click()

    def go_to_new(self):
        with allure.step('Переход в категорию "Новинки"'):
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_btn))).click()
    def go_to_pocketbooks(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pocketbooks_btn))).click()
    def go_to_accessories(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accessories_btn))).click()
    def get_search_field(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field))).click()
    def input(self, search_text):
        self.get_search_field().send_keys(search_text)
        self.get_search_field().send_keys(Keys.ENTER)
