import time

from assertpy import assert_that

from lesson_27.pages.main_page import MainPage
from lesson_27.pages.search_page import SearchPage
from lesson_27.tests.conftest import web_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestSearch:
    main_page: MainPage
    search_page: SearchPage


    def test_that_parcl_is_delivered(self, web_driver):
        self.main_page = MainPage(web_driver)

        self.main_page.fill_search_field()

        self.search_page = SearchPage(web_driver)

        WebDriverWait(web_driver, timeout=10).until(EC.url_contains("/chat/messages"))

        assert_that(self.search_page.status_of_parcel_text(), f'Not received, try again').is_equal_to("Отримана")



