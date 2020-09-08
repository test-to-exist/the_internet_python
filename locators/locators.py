from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, 'Add/Remove Elements')
    BROKEN_IMAGES = (By.LINK_TEXT, 'Broken Images')
    CHECKBOXES = (By.LINK_TEXT, 'Checkboxes')


class AddRemoveElementsLocators:
    EXAMPLE_BUTTON = (By.CSS_SELECTOR, 'div.example > button')
    ADDED_MANUALLY_BUTTONS = (By.CSS_SELECTOR, 'div#elements > button.added-manually')


class BrokenImagesLocators:
    EXAMPLE_IMAGES = (By.CSS_SELECTOR, 'div.example > img')


class CheckboxesPageLocators:
    # CHECKBOXES_NAMES = (By.XPATH, "//input[@type='checkbox']")

    @staticmethod
    def get_checkbox_with_inner_text(inner_text: str):
        return By.XPATH, f"//input[@type='checkbox'][contains(normalize-space(following-sibling::text()),'{inner_text}')]"
