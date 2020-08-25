import unittest

from selenium import webdriver

from pages.broken_images import BrokenImages
from pages.main import MainPage


class BrokenImagesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_broken_images(self):
        main_page = MainPage(self.driver, 'http://the-internet.herokuapp.com')
        main_page.go_to_page('broken_images')

        broken_images_page = BrokenImages(self.driver, 'http://the-internet.herokuapp.com')
        broken_images_page.check_broken_images()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
