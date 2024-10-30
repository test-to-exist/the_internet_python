from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest

from pages.disappearing_elements.disappearing_elements_page import DisappearingElementsPage

from tests.base_test_case import BaseTestCase


class DisappearingElementsTests(BaseTestCase):
    def test_user_redirected_to_home_page(self):
        self.driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        self.disappearing_elements_page = DisappearingElementsPage(self.driver)
        main_page = self.disappearing_elements_page.home()
        self.assertTrue(main_page.is_header_visible())

    def test_user_redirected_to_not_found_after_about(self):
        self.driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        self.disappearing_elements_page = DisappearingElementsPage(self.driver)
        about_page = self.disappearing_elements_page.about()
        self.assertTrue(about_page.is_header_visible())

    def test_user_redirected_to_not_found_after_contact_us(self):
        self.driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        self.disappearing_elements_page = DisappearingElementsPage(self.driver)
        contact_us_page = self.disappearing_elements_page.contact_us()
        self.assertTrue(contact_us_page.is_header_visible())

    def test_user_redirected_to_not_found_after_portfolio(self):
        self.driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        self.disappearing_elements_page = DisappearingElementsPage(self.driver)
        portfolio_page = self.disappearing_elements_page.portfolio()
        self.assertTrue(portfolio_page.is_header_visible())

    def test_gallery_link_shows_and_disappears_randomly(self):
        self.driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        self.disappearing_elements_page = DisappearingElementsPage(self.driver)
        refresh_page_count = 10
        gallery_link_visible_count = 0

        for _ in range(refresh_page_count):
            self.driver.refresh()
            if self.disappearing_elements_page.is_gallery_visible():
                gallery_link_visible_count += 1

        print(f"Gallery link appeared {gallery_link_visible_count} times")
        self.assertGreater(gallery_link_visible_count, 0)