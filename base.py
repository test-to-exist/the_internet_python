from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver: WebDriver = driver
        self.base_url: str = base_url
