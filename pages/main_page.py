from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def click_link(self, locator: By):
        link = self.driver.find_element(*locator)
        link.click()

