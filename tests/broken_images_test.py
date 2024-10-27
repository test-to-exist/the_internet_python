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

        response1 = requests.head(images[0])
        assert response1.status_code == 404
        response2 = requests.head(images[1])
        assert response2.status_code == 404
        response3 = requests.head(images[2])
        assert response3.status_code == 200


if __name__ == '__main__':
    unittest.main()
