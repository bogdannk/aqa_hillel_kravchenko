import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from lesson_27.tast_data.test_data import TestData


@pytest.fixture(scope="session")
def web_driver():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield driver

    driver.quit()