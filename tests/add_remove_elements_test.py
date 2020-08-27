import time
import unittest

from locators.locators import MainPageLocators
from pages.add_remove_elements import AddRemoveElements
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class AddRemoveElementsTest(BaseTestCase):

    def test_add_remove_elements(self):
        main_page = MainPage(self.driver)
        main_page.go_to_page(MainPageLocators.ADD_REMOVE_ELEMENTS)

        add_remove_elements_page = AddRemoveElements(self.driver)
        add_remove_elements_page.click_add_element_btn(10)
        time.sleep(1)
        add_remove_elements_page.click_all_delete_buttons()


if __name__ == '__main__':
    unittest.main()
