from locators.locators import BrokenImagesLocators
from pages.base_page import BasePage


class BrokenImages(BasePage):

    def get_images_links(self):
        images = self.driver.find_elements(*BrokenImagesLocators.EXAMPLE_IMAGES)
        res = []
        for img in images:
            res.append(img.get_attribute('src'))
        return res
