from locators.locators import ChallengingDomLocators
from pages.base_page import BasePage


class ChallengingDom(BasePage):
    def click_first_button(self):
        self.driver.find_element(*ChallengingDomLocators.FIRST_BUTTON).click()

    def click_edit_link(self, link_number):
        self.driver.find_elements(*ChallengingDomLocators.EDIT_BUTTONS)[link_number].click()