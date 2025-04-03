from typing import Optional

import allure

from Helpers.request import Request


class PostAPI(Request):
    @allure.step("Отправить запрос на создание объекта")
    def create_data(self, title: str, verified: Optional[bool] = True):
        return self.send_post_request("api/create/", title, verified)
