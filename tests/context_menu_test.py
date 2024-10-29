from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.locators import MainPageLocators
from pages.context_menu_page import ContextMenuPage
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class ContextMenuTests(BaseTestCase):
    def test_user_should_see_context_menu_alert(self):
        main_page = MainPage(self.driver)
        main_page.click_link(MainPageLocators.CONTEXT_MENU)
        self.context_menu_page = ContextMenuPage(self.driver)
        self.context_menu_page.show_context_menu()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.assertIn('You selected a context menu', alert.text)
        alert.accept()

