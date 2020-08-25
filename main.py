from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


def add_remove_elements(url, driver):
    route = '/add_remove_elements/'
    driver.get(f"{url}{route}")
    example_btn = driver.find_element_by_css_selector('div.example > button')

    for i in range(0, 7):
        example_btn.click()
        time.sleep(0.2)

    time.sleep(0.5)
    elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#elements > button.added-manually')))

    for el in elements:
        el.click()
        time.sleep(0.2)


def broken_images(url, driver):
    route = '/broken_images'
    driver.get(f"{url}{route}")
    elements: list[WebElement] = driver.find_elements_by_css_selector('div.example > img')

    for el in elements:
        response = requests.head(el.get_attribute('src'))
        print(response.status_code)
        assert response.status_code == 200


if __name__ == '__main__':
    base_url = 'http://the-internet.herokuapp.com'
    driver = webdriver.Chrome()
    # add_remove_elements(base_url, driver)
    broken_images(base_url, driver)
