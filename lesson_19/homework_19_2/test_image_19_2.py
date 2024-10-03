import requests
from requests import Response
from assertpy import assert_that
import os

class TestImageApi:

    __base_url = 'http://127.0.0.1:8080'
    __upload_url = f'{__base_url}/upload'
    __get_url_template = f'{__base_url}/image/{{}}'
    __delete_url_template = f'{__base_url}/delete/{{}}'
    __test_image_path = '/Users/bogdankravcenko/Downloads/sunset.jpg'  # Change this to your test image path

    def test_upload_image_status_code(self):
        with open(self.__test_image_path, 'rb') as img_file:
            files = {'image': img_file}
            response: Response = requests.post(self.__upload_url, files=files)
        (assert_that(response.status_code, f"Expected status code 201, but got {response.status_code}")
         .is_equal_to(201))

    def test_upload_image_contains_image_url(self):
        with open(self.__test_image_path, 'rb') as img_file:
            files = {'image': img_file}
            response: Response = requests.post(self.__upload_url, files=files)
        image_data = response.json()
        print(f"Response data: {image_data}")  # Print the response for debugging
        assert_that(image_data).contains_key('image_url')

    def test_upload_image_without_file(self):
        response: Response = requests.post(self.__upload_url, files={})
        (assert_that(response.status_code, f"Expected status code 400, but got {response.status_code}")
         .is_equal_to(400))
        error_data = response.json()
        print(f"Response data: {error_data}")
        assert_that(error_data, 'Response should contain an error message').contains_key('error')

    def test_delete_image_success(self):
        with open(self.__test_image_path, 'rb') as img_file:
            upload_response = requests.post(self.__upload_url, files={'image': img_file})
            assert_that(upload_response.status_code, "Image upload failed").is_equal_to(201)
        filename = os.path.basename(self.__test_image_path)
        delete_url = self.__delete_url_template.format(filename)

        response: Response = requests.delete(delete_url)

        message_data = response.json()
        assert_that(message_data, 'Response should contain a success message').is_equal_to({'message': 'Image sunset.jpg deleted'})




