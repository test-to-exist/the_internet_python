import requests
from selenium.webdriver.remote.webelement import WebElement

from base import BasePage


class BrokenImages(BasePage):

    def check_broken_images(self):
        elements: list[WebElement] = self.driver.find_elements_by_css_selector('div.example > img')

        for el in elements:
            response = requests.head(el.get_attribute('src'))
            print(response.status_code)
            assert response.status_code == 200
