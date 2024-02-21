import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.close()
