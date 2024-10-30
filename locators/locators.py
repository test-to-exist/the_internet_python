from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, 'Add/Remove Elements')
    BROKEN_IMAGES = (By.LINK_TEXT, 'Broken Images')
    CHECKBOXES = (By.LINK_TEXT, 'Checkboxes')
    CHALLENGING_DOM = (By.LINK_TEXT, 'Challenging DOM')
    CONTEXT_MENU = (By.LINK_TEXT, 'Context Menu')
    DISAPPEARING_ELEMENTS = (By.LINK_TEXT, 'Disappearing Elements')
    HEADER = (By.XPATH,'//h1[contains(text(),"Welcome to the-internet")]')


class AddRemoveElementsLocators:
    EXAMPLE_BUTTON = (By.CSS_SELECTOR, 'div.example > button')
    ADDED_MANUALLY_BUTTONS = (By.CSS_SELECTOR, 'div#elements > button.added-manually')


class BrokenImagesLocators:
    EXAMPLE_IMAGES = (By.CSS_SELECTOR, 'div.example > img')


class CheckboxesPageLocators:
    @staticmethod
    def get_checkbox_with_inner_text(inner_text: str):
        return By.XPATH, f"//input[@type='checkbox'][contains(normalize-space(following-sibling::text()),'{inner_text}')]"


class ChallengingDomLocators:
    FIRST_BUTTON = (By.CSS_SELECTOR, '.button:first-of-type')
    EDIT_BUTTONS = (By.LINK_TEXT, 'edit')

class DisappearingElementsLocators:
    ABOUT_PAGE_HEADER = (By.XPATH, '//h1[contains(text(),"Not Found")]')
    CONTACT_US_PAGE_HEADER = (By.XPATH, '//h1[contains(text(),"Not Found")]')
    GALLERY_PAGE_HEADER = (By.XPATH, '//h1[contains(text(),"Not Found")]')
    PORTFOLIO_PAGE_HEADER = (By.XPATH, '//h1[contains(text(),"Not Found")]')
