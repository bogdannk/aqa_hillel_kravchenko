from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.pages.abstract_page import AbstractPage
from lesson_28.test_data.tese_data import TestData
from lesson_28.web_element.abstract_element import AbstractElement


class MainPage(AbstractPage, AbstractElement):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._wrapped_element = AbstractElement(driver)



    sign_in_button_locator: tuple[str, str] = (By.XPATH, ".//button[contains(text(),'Sign In')]")
    sign_up_button_locator: tuple[str, str] = (By.XPATH, ".//button[contains(text(),'Sign up')]")
    user_first_name_field_locator: tuple[str, str] = (By.XPATH, ".//input[@id = 'signupName']")
    user_last_name_field_locator: tuple[str, str] = (By.XPATH, ".//input[@id = 'signupLastName']")
    user_email_field_locator: tuple[str, str] = (By.XPATH, ".//input[@id = 'signupEmail']")
    sign_up_password_field_locator: tuple[str, str] = (By.XPATH, ".//input[@id = 'signupPassword']")
    sign_up_repeat_password_field_locator: tuple[str, str] = (By.XPATH, ".//input[@id = 'signupRepeatPassword']")
    register_button_locator: tuple[str, str] = (By.XPATH, ".//button[contains(text(),'Register')]")

    @property
    def sign_up_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.sign_up_button_locator)

    def click_on_sign_up_button(self):
        self._wrapped_element.wait_to_be_clicable(self.sign_up_button)
        self.sign_up_button.click()

    def fill_user_first_name_field(self):
        user_first_name_field: WebElement = self._wrapped_element.find_element(self.user_first_name_field_locator)
        user_first_name_field.send_keys(TestData.USER_FIRST_NAME)

    def fill_user_last_name_field(self):
        user_last_name_field: WebElement = self._wrapped_element.find_element(self.user_last_name_field_locator)
        user_last_name_field.send_keys(TestData.USER_LAST_NAME)

    def fill_user_email_field(self):
        user_email_field: WebElement = self._wrapped_element.find_element(self.user_email_field_locator)
        user_email_field.send_keys(TestData.USER_EMAIL)

    def fill_sign_up_password_field(self):
        sign_up_password_field: WebElement = self._wrapped_element.find_element(self.sign_up_password_field_locator)
        sign_up_password_field.send_keys(TestData.PASSWORD)

    def fill_sign_up_repeat_password_field(self):
        sign_up_repeat_password_field: WebElement = self._wrapped_element.find_element(self.sign_up_repeat_password_field_locator)
        sign_up_repeat_password_field.send_keys(TestData.PASSWORD)

    @property
    def register_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.register_button_locator)

    def click_on_register_button(self):
        self._wrapped_element.wait_to_be_clicable(self.register_button)
        self.register_button.click()


    def new_user_registration(self):
        self.click_on_sign_up_button()
        self.fill_user_first_name_field()
        self.fill_user_last_name_field()
        self.fill_user_email_field()
        self.fill_sign_up_password_field()
        self.fill_sign_up_repeat_password_field()
        self.click_on_register_button()







