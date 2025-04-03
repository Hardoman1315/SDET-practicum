import allure

from Helpers.request import Request


class DelAPI(Request):
    @allure.step("Отправить запрос на удаление объекта по ID")
    def del_by_id(self, entry_id: str):
        return self.send_delete_request("api/delete/", entry_id)
