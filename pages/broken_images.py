import requests
from selenium.webdriver.remote.webelement import WebElement

from locators.locators import BrokenImagesLocators
from pages.base_page import BasePage


class BrokenImages(BasePage):

    def check_broken_images(self):
        elements: list[WebElement] = self.driver.find_elements(*BrokenImagesLocators.EXAMPLE_IMAGES)

        for el in elements:
            response = requests.head(el.get_attribute('src'))
            assert response.status_code == 200
