import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.pages.abstract_page import AbstractPage
from selenium.webdriver.common.by import By

from lesson_27.tast_data.test_data import TestData


class MainPage(AbstractPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)


    search_fild_locator: tuple[str, str] = (By.XPATH, ".//input[@placeholder='Номер посилки']")
    search_button_locator: tuple[str, str] = (By.XPATH, ".//input[@ value = 'Пошук']")

    def fill_search_field(self, ):
        search_field: WebElement = self._wrapped_element.find_element(self.search_fild_locator)
        search_field.send_keys(TestData.parcel_number)

        search_button: WebElement = self._wrapped_element.find_element(self.search_button_locator)
        self._wrapped_element.wait_to_be_clicable(search_button)

        search_button.click()





