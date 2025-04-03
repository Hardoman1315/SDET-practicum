import allure

from Helpers.request import Request


class GetAPI(Request):
    @allure.step("Получить информацию об объекте по ID")
    def get_by_id(self, entry_id: str = "1"):
        return self.send_get_request("api/get/", entry_id)

    @allure.step("Получить информацию о каждом объекте в таблицах")
    def get_all(self):
        return self.send_get_request("api/getAll/")
