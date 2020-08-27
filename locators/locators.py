from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, 'Add/Remove Elements')
    BROKEN_IMAGES = (By.LINK_TEXT, 'Broken Images')


class AddRemoveElementsLocators:
    EXAMPLE_BUTTON = (By.CSS_SELECTOR, 'div.example > button')
    ADDED_MANUALLY_BUTTONS = (By.CSS_SELECTOR, 'div#elements > button.added-manually')


class BrokenImagesLocators:
    EXAMPLE_IMAGES = (By.CSS_SELECTOR, 'div.example > img')
