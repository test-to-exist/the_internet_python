from base import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage(BasePage):
    def go_to_page(self, route: str):
        self.driver.get(f"{self.base_url}/{route}")
