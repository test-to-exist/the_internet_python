import unittest

from locators.locators import MainPageLocators
from pages.checkboxes_page import Checkboxes
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class CheckboxesTest(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.checkboxes_page = None
        self.checkboxes_names = [
            'checkbox 1',
            'checkbox 2'
        ]

    def check_if_checkbox_works(self, text):

        if self.checkboxes_page.checkbox_is_checked(text):
            self.checkboxes_page.click_checkbox(text)
            assert not self.checkboxes_page.checkbox_is_checked(text)
        else:
            self.checkboxes_page.click_checkbox(text)
            assert self.checkboxes_page.checkbox_is_checked(text)

    def test_checkboxes(self):
        main_page: MainPage = MainPage(self.driver)
        main_page.click_link(MainPageLocators.CHECKBOXES)
        self.checkboxes_page: Checkboxes = Checkboxes(self.driver)
        for name in self.checkboxes_names:
            self.check_if_checkbox_works(name)


if __name__ == '__main__':
    unittest.main()
