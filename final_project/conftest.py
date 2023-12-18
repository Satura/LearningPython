import pytest
from sys import platform
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import Home_page
from pages.login_page import Login_page


@pytest.fixture()
def set_up():
    print('Start')

    # driver_path = ''
    # if platform == 'linux':
    #     driver_path = '.././webdriver/geckodriver'
    # elif platform == 'win32':
    #     driver_path = '.././webdriver/geckodriver.exe'
    # driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=driver_path))

    # print('Start login')
    # hp = Home_page(driver)
    # lp = Login_page(driver)
    # hp.open_site()
    # hp.go_to_auth()
    # lp.authorization()
    # assert driver.find_element(By.XPATH, hp.profile_link).is_displayed()
    # print('We login')

    yield

    # driver.quit()
    print('Finish')