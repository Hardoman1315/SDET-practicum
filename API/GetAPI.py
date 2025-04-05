import allure

from Helpers.request import Request
from data.api_paths import api_get, api_get_all


class GetAPI(Request):
    @allure.step("Получить информацию об объекте по ID")
    def get_by_id(self, entry_id: str = "1"):
        return self.send_get_request(api_get, entry_id)

    @allure.step("Получить информацию о каждом объекте в таблицах")
    def get_all(self):
        return self.send_get_request_list(api_get_all)
