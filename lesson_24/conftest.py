import pytest
import requests
import logging
from requests import Response, Session
from assertpy import assert_that
from requests.auth import HTTPBasicAuth



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test_search.log"),
        logging.StreamHandler()
    ]
)

BASE_URL: str = "http://127.0.0.1:8080"

@pytest.fixture(scope="session", autouse=True)
def authorization():
    auth = HTTPBasicAuth('test_user', 'test_pass')

    response: Response = requests.post(f"{BASE_URL}/auth", auth=auth, verify=False)

    assert_that(response.status_code).is_equal_to(200)
    access_token = response.json().get("access_token")

    current_session = Session()
    current_session.headers.update({'Authorization': 'Bearer ' + access_token})

    yield current_session

    logging.info("Authorization completed.")


