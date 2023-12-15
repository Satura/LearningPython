from selenium import webdriver
from sys import platform

class Base():
    def __init__(self, driver):
        self.driver = driver

    INDILOGIN = '***'
    INDIPASS = '***'
