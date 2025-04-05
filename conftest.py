import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')

    if os.getenv('CI_ENV') == 'true':
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    _driver = webdriver.Chrome(options=options)
    _driver.minimize_window()
    yield _driver
    _driver.quit()


@pytest.fixture
def fixture_delete():
    from API.DelAPI import DelAPI
    from data.api_paths import api_delete

    api = DelAPI()

    class DeleteFixture:
        @staticmethod
        def del_by_id(entry_id: str):
            response = api.send_delete_request(api_delete, entry_id)
            assert response == 204, (
                f"[ERROR] Сервер вернул неожиданный код ({response})"
            )

        @staticmethod
        def check_del(entry_id: str):
            response = api.send_delete_request(api_delete, entry_id)
            assert response == 500, (
                f"[ERROR] Сервер вернул неожиданный код ({response})"
            )

    return DeleteFixture()


@pytest.fixture
def fixture_post():
    from API.PostAPI import PostAPI
    from API.GetAPI import GetAPI
    from typing import Optional
    from data.api_paths import api_create

    post_api = PostAPI();
    get_api = GetAPI()

    class PostFixture:
        @staticmethod
        def create_data(title: str, verified: Optional[bool] = True):
            response = post_api.send_post_request(api_create, title, verified)
            assert get_api.get_by_id(response).title == title and get_api.get_by_id(response).entry_id == response, (
                "[ERROR] Данные созданной записи не совпадают"
            )
            return response

    return PostFixture()
