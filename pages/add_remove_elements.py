from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base import BasePage
from time import time


class AddRemoveElements(BasePage):

    def add_and_remove(self):
        example_btn = self.driver.find_element_by_css_selector('div.example > button')

        for i in range(0, 7):
            example_btn.click()
            time.sleep(0.2)

        time.sleep(0.5)
        elements = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#elements > button.added-manually')))

        for el in elements:
            el.click()
            time.sleep(0.2)
