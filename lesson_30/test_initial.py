import pytest
import allure

@allure.feature("This test class is for allure learning")
class TestInitial:
    @allure.story("This test for sum function validation")
    @pytest.mark.parametrize("input_data, expected_output", [
        ([1, 2, 3], 6),
        ([-1, 0, 1], 0),
        ([10, 20, 30], 60)
    ])

    def test_sum(self, input_data, expected_output):
        assert sum(input_data) == expected_output

    @allure.story("This test for apper case validation")
    @pytest.mark.parametrize("input_string, expected_output", [
        ("hello", "HELLO"),
        ("world", "WORLD")
    ])
    def test_uppercase(self, input_string, expected_output):
        assert input_string.upper() == expected_output