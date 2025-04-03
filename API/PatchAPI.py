from typing import Optional

import allure

from Helpers.request import Request
from data.api_paths import api_patch


class PatchAPI(Request):
    @allure.step("Отправить запрос на изменение объекта по id")
    def patch_data(self, entry_id: str, title: str, verified: Optional[bool] = None):
        return self.send_patch_request(api_patch, entry_id, title, verified)
