import time

from locators.locators import AddRemoveElementsLocators
from pages.base_page import BasePage


class AddRemoveElements(BasePage):

    def click_add_element_btn(self, nb_times=7):
        example_btn = self.driver.find_element(*AddRemoveElementsLocators.EXAMPLE_BUTTON)

        for i in range(0, nb_times):
            example_btn.click()
            time.sleep(0.2)

    def click_all_delete_buttons(self):
        delete_buttons = self.driver.find_elements(*AddRemoveElementsLocators.ADDED_MANUALLY_BUTTONS)
        for btn in delete_buttons:
            btn.click()
            time.sleep(0.2)
