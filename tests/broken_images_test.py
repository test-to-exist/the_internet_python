import unittest

import requests

from locators.locators import MainPageLocators
from pages.broken_images import BrokenImages
from pages.main_page import MainPage
from tests.base_test_case import BaseTestCase


class BrokenImagesTest(BaseTestCase):

    def test_broken_images(self):
        main_page = MainPage(self.driver)
        main_page.click_link(MainPageLocators.BROKEN_IMAGES)

        broken_images_page = BrokenImages(self.driver)
        images = broken_images_page.get_images_links()

        for img in images:
            response = requests.head(img)
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
