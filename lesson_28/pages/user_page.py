from lesson_28.pages.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.web_element.abstract_element import AbstractElement

class UserPage(AbstractPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wrapped_element = AbstractElement(driver)

    my_profile_dropdown_menu_button_locator: tuple[str, str] = (By.XPATH, ".//button[@id = 'userNavDropdown']")
    profile_option_menu_locator: tuple[str, str] = (By.XPATH, ".//div//a[text() = 'Profile']")
    logout_button_locator: tuple[str, str] = (By.XPATH, ".//button[contains(text(),'Logout')]")
    profile_name_locator: tuple[str, str] = (By.XPATH, ".//div//p[contains(@class,'profile_name')]")

    @property
    def my_profile_dropdown_menu_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.my_profile_dropdown_menu_button_locator)

    def click_on_my_profile_menu(self):
        self._wrapped_element.wait_for_visible(self.my_profile_dropdown_menu_button)
        self.my_profile_dropdown_menu_button.click()

    @property
    def logout_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.logout_button_locator)

    @property
    def profile_option_menu(self) -> WebElement:
        return self._wrapped_element.find_element(self.profile_option_menu_locator)

    def get_profile_name_text(self):
        self._wrapped_element.wait_for_visible(self.profile_option_menu)
        self.profile_option_menu.click()

        profile_text: str = self._wrapped_element.find_element(self.profile_name_locator).text
        return profile_text




