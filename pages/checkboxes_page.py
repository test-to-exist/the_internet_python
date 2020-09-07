from selenium.webdriver.remote.webelement import WebElement

from locators.locators import CheckboxesPageLocators
from pages.base_page import BasePage


class Checkboxes(BasePage):

    def get_checkboxes_list(self):
        return self.driver.find_elements(*CheckboxesPageLocators.CHECKBOXES)

    def checkbox_is_checked(self, inner_text):
        checkbox = self.driver.find_element(*CheckboxesPageLocators.get_checkbox_with_inner_text(inner_text))
        return checkbox.get_property("checked")

    def click_checkbox(self, inner_text):
        self.driver.find_element(*CheckboxesPageLocators.get_checkbox_with_inner_text(inner_text)).click()
