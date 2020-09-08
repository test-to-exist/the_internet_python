import time

from selenium.webdriver.remote.webdriver import WebDriver

from locators.locators import AddRemoveElementsLocators
from pages.base_page import BasePage


class AddRemoveElements(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.example_btn = self.driver.find_element(*AddRemoveElementsLocators.EXAMPLE_BUTTON)

    def click_add_element_btn(self):
        self.example_btn.click()
        time.sleep(0.2)

    def get_delete_btn_nb(self):
        delete_buttons = self.driver.find_elements(*AddRemoveElementsLocators.ADDED_MANUALLY_BUTTONS)
        return len(delete_buttons)

    def click_delete_button(self):
        delete_buttons = self.driver.find_elements(*AddRemoveElementsLocators.ADDED_MANUALLY_BUTTONS)
        delete_buttons[0].click()
        time.sleep(0.2)
