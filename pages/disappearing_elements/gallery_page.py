from selenium.webdriver.remote.webdriver import WebDriver

from locators.locators import DisappearingElementsLocators
from pages.base_page import BasePage


class GalleryPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = self.driver.find_element(*DisappearingElementsLocators.GALLERY_PAGE_HEADER)