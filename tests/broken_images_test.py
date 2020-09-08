import unittest

from locators.locators import MainPageLocators
from pages.broken_images import BrokenImages
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class BrokenImagesTest(BaseTestCase):

    def test_broken_images(self):
        main_page = MainPage(self.driver)
        main_page.click_link(MainPageLocators.BROKEN_IMAGES)

        broken_images_page = BrokenImages(self.driver)
        broken_images_page.check_broken_images()


if __name__ == '__main__':
    unittest.main()
