from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


from pages.base_page import BasePage

from pages.main_page import MainPage
from pages.disappearing_elements.contact_us_page import ContactUsPage
from pages.disappearing_elements.about_page import AboutPage
from pages.disappearing_elements.portfolio_page import PortfolioPage



class DisappearingElementsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.home_button = driver.find_element(By.LINK_TEXT, "Home")
        self.about_button = driver.find_element(By.LINK_TEXT, "About")
        self.contact_us_button = driver.find_element(By.LINK_TEXT, "Contact Us")
        self.portfolio_button = driver.find_element(By.LINK_TEXT, "Portfolio")

    def home(self):
        self.home_button.click()
        return MainPage(self.driver)

    def about(self):
        self.about_button.click()
        return AboutPage(self.driver)

    def contact_us(self):
        self.contact_us_button.click()
        return ContactUsPage(self.driver)

    def portfolio(self):
        self.portfolio_button.click()
        return PortfolioPage(self.driver)

    def is_gallery_visible(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "Gallery").is_displayed()
            return self.driver.find_element(By.LINK_TEXT, "Gallery").is_displayed()
        except:
            return False