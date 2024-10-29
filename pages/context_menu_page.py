from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.hot_spot = self.driver.find_element(By.ID, 'hot-spot')

    def show_context_menu(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.hot_spot).context_click().perform()