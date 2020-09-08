import time
import unittest

from locators.locators import MainPageLocators
from pages.add_remove_elements import AddRemoveElements
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class AddRemoveElementsTest(BaseTestCase):

    def test_add_remove_elements(self):
        main_page = MainPage(self.driver)
        main_page.click_link(MainPageLocators.ADD_REMOVE_ELEMENTS)

        add_remove_elements_page = AddRemoveElements(self.driver)
        nb_clicks = 7
        for i in range(0, nb_clicks):
            add_remove_elements_page.click_add_element_btn()
        time.sleep(1)
        assert add_remove_elements_page.get_delete_btn_nb() == nb_clicks

        for i in range(0, nb_clicks):
            add_remove_elements_page.click_delete_button()
        assert add_remove_elements_page.get_delete_btn_nb() == 0


if __name__ == '__main__':
    unittest.main()
