from locators.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class MainPage(BasePage):
    def __init__(self, driver: WebDriver ):
        super().__init__(driver)
        self.header = self.driver.find_element(*MainPageLocators.HEADER)

    def click_link(self, locator: By):
        link = self.driver.find_element(*locator)
        link.click()

