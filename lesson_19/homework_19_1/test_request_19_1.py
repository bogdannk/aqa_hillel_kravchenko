import requests
from requests import Response
from assertpy import assert_that


class TestApiResponse:

    __base_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    __params = {
        'sol': 1000,
        'camera': 'fhaz',
        'api_key': 'DEMO_KEY'
    }

    def test_response_status_code_is_200(self):
        response: Response = requests.get(self.__base_url, params=self.__params)

        (assert_that(response.status_code, f"Request was unsuccessful and stats code was {response.status_code}")
         .is_equal_to(200))

    def test_response_status_code_without_params_is_equal_to_403(self):
        response: Response = requests.get(self.__base_url)

        (assert_that(response.status_code, f"Status code should be 403, but was{response.status_code}")
         .is_equal_to(403))

    def test_response_is_not_empty(self):
        response: Response = requests.get(self.__base_url, params=self.__params)
        response_data = response.json()
        assert_that(response_data,"Error, response data is empty").is_not_empty()

    def test_response_img_src_in_response(self):
        search_data = 'img_src'

        response: Response = requests.get(self.__base_url, params=self.__params)
        response_data = response.json()
        photos = response_data.get('photos', [])
        (assert_that(any(search_data in photo for photo in photos),
                f"Error, search data {search_data} is not in response"))