from locators.locators import ChallengingDomLocators
from pages.base_page import BasePage


class ChallengingDom(BasePage):
    def click_first_button(self):
        self.driver.find_element(ChallengingDomLocators.FIRST_BUTTON).click()
