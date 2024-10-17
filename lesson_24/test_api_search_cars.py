import pytest
import logging
from assertpy import assert_that
from requests import Response
from lesson_24.conftest import BASE_URL


class TestCarAPISearch:

    @pytest.mark.parametrize("sort_by, limit, expected_count", [
        ("price", 5, 5),
        ("year", 10, 10),
        ("engine_volume", 3, 3),
        (None, 4, 4),
        ("brand", 7, 7),
        ("price", 0, 0),
    ])
    def test_get_cars(self, authorization, sort_by, limit, expected_count):
        response: Response = authorization.get(f"{BASE_URL}/cars", params={"sort_by": sort_by, "limit": limit})

        logging.info(f"Testing with sort_by={sort_by} and limit={limit}")
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response data: {response.json()}")

        assert_that(response.status_code).is_equal_to(200)
        response_data = response.json()

        assert_that(isinstance(response_data, list)).is_true()

        assert_that(len(response_data)).is_equal_to(expected_count)

    def test_get_cars_empty_response(self, authorization):
        response: Response = authorization.get(f"{BASE_URL}/cars", params={"sort_by": "price", "limit": 0})

        logging.info("Testing with limit=0 to check for empty response")
        assert_that(response.status_code).is_equal_to(200)
        response_data = response.json()
        assert_that(response_data).is_equal_to([])

    def test_get_cars_response_structure(self, authorization):
        response: Response = authorization.get(f"{BASE_URL}/cars", params={"sort_by": "price", "limit": 5})

        logging.info("Testing response structure")
        assert_that(response.status_code).is_equal_to(200)
        response_data = response.json()

        for car in response_data:
            assert_that("brand" in car).is_true()
            assert_that("price" in car).is_true()
            assert_that("year" in car).is_true()
            assert_that("engine_volume" in car).is_true()

    def test_get_cars_sorted_by_price(self, authorization):
        response: Response = authorization.get(f"{BASE_URL}/cars", params={"sort_by": "price", "limit": 10})

        logging.info("Testing cars sorted by price")
        assert_that(response.status_code).is_equal_to(200)
        response_data = response.json()

        # Проверка, что список отсортирован по возрастанию цены
        prices = [car["price"] for car in response_data]
        assert_that(prices).is_equal_to(sorted(prices))
