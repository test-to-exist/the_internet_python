from locators.locators import BrokenImagesLocators
from pages.base_page import BasePage


class BrokenImages(BasePage):

    def get_images_links(self):
        return map(lambda el: el.get_attribute('src'), self.driver.find_elements(*BrokenImagesLocators.EXAMPLE_IMAGES))
