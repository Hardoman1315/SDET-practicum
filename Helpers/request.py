import json
from typing import Optional

import allure
import requests

from Helpers.Models import Entries, Entry, Pattern


class Request:
    def __init__(self, url='http://localhost:8080/'):
        self.url = url

    @allure.step("Отправить POST-запрос")
    def send_post_request(self, path: str, title: str, verified: Optional[bool] = True):
        complete_url = self.url + path
        response = requests.post(complete_url, json=json.loads(self.__internal_complete_pattern(
            title, verified)))
        assert response.status_code == 200, (
            f"[ERROR] Сервер вернул неожиданный код ({response.status_code})"
        )
        return response.json()

    @allure.step("Отправить PATCH-запрос")
    def send_patch_request(self, path: str, entry_id: str, title: str, verified: Optional[bool] = True):
        complete_url = f"{self.url}{path}{entry_id}"
        response = requests.patch(complete_url, json=json.loads(self.__internal_complete_pattern(
            title, verified)))
        assert response.status_code == 204, (
            f"[ERROR] Сервер вернул неожиданный код ({response.status_code})"
        )

    @allure.step("Отправить GET-запрос")
    def send_get_request(self, path: str, payload: str = None):
        complete_url = f"{self.url}{path}{payload}"
        response = requests.get(complete_url)
        assert response.status_code == 200, (
            f"[ERROR] Сервер вернул неожиданный код ({response.status_code})"
        )
        return Entry.model_validate(response.json())

    @allure.step("Отправить GET-запрос на список")
    def send_get_request_list(self, path: str):
        complete_url = f"{self.url}{path}"
        response = requests.get(complete_url)
        assert response.status_code == 200, (
            f"[ERROR] Сервер вернул неожиданный код ({response.status_code})"
        )
        json_data = Entries.model_validate(response.json())
        return json_data.entity

    @allure.step("Отправить DELETE-запрос")
    def send_delete_request(self, path: str, payload: str):
        complete_url = f"{self.url}{path}{payload}"
        response = requests.delete(complete_url)
        assert response.status_code == 204 or 500, (
            "[ERROR] Сервер вернул неожиданный код"
        )
        return response.status_code

    @staticmethod
    def __internal_complete_pattern(title: str, verified: Optional[bool] = True):
        result = Pattern(
            addition={},
            important_numbers=[],
            title=title,
            verified=verified
        ).model_dump_json()
        return result
