import unittest

from locators.locators import MainPageLocators
from pages.challenging_dom import ChallengingDom
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class ChallengingDomTest(BaseTestCase):
    def test_first_button(self):
        main_page = MainPage(self.driver)
        main_page.click_link(MainPageLocators.CHALLENGING_DOM)

        challenging_dom_page = ChallengingDom(self.driver)
        challenging_dom_page.click_first_button()


if __name__ == '__main__':
    unittest.main()
