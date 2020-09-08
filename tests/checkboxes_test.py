import time
import unittest

from locators.locators import MainPageLocators
from pages.checkboxes_page import Checkboxes
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class CheckboxesTest(BaseTestCase):

    def check_if_checkbox_works(self, text):
        checkboxes_page: Checkboxes = Checkboxes(self.driver)
        if checkboxes_page.checkbox_is_checked(text):
            checkboxes_page.click_checkbox(text)
            assert not checkboxes_page.checkbox_is_checked(text)
        else:
            checkboxes_page.click_checkbox(text)
            assert checkboxes_page.checkbox_is_checked(text)

    def test_if_checkboxes_work(self):
        main_page: MainPage = MainPage(self.driver)
        main_page.click_link(MainPageLocators.CHECKBOXES)
        self.check_if_checkbox_works('checkbox 1')
        time.sleep(1)
        self.check_if_checkbox_works('checkbox 2')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
