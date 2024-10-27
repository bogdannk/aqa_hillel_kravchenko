from lesson_27.pages.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.web_element.abstract_element import AbstractElement


class SearchPage(AbstractPage, AbstractElement):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    parcel_status_locator: tuple[str, str] = (By.XPATH, ".//div[@class = 'header__status-text']")
    confirmation_locator: tuple[str, str] = (By.XPATH, ".//span[@class = 'v-btn__content']")
    @property
    def confirmation_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.confirmation_locator)

    def status_of_parcel_text(self):
        self._wrapped_element.wait_to_be_clicable(self.confirmation_button)
        self.confirmation_button.click()

        status_of_parsel: str = self._wrapped_element.find_element(self.parcel_status_locator).text
        return status_of_parsel

