import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

from lesson_28.test_data.tese_data import TestData


@pytest.fixture(scope="session")
def web_driver():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield driver

    driver.quit()