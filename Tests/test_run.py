import allure

from API.DelAPI import DelAPI
from API.GetAPI import GetAPI
from API.PatchAPI import PatchAPI
from API.PostAPI import PostAPI
from Helpers.Generator import Generator
from Pages.Manager.AddClient.AddClient import AddClient
from Pages.Manager.DeleteClient.DeleteClient import DeleteClient
from Pages.Manager.SortClients.SortClients import SortClients


@allure.suite("Набор UI-тестов")
class TestsUI:
    @allure.title("Добавить клиента")
    async def test_add_customer(self, driver):
        customer_driver = AddClient(driver)

        customer_driver.open_target_page()
        code = Generator.generate_code()
        customer_driver.click_add_customer()
        customer_driver.fill_all_fields(code)
        customer_driver.confirm_adding()
        customer_driver.close_alert()
        customer_driver.click_customers_btn()
        customer_driver.check_new_customer_existence(code)
        customer_driver.clear_test_entities(code)

    @allure.title("Сортировать пользователей по имени")
    async def test_sort_customers(self, driver):
        sort_driver = SortClients(driver)

        sort_driver.open_target_page()
        sort_driver.click_customers_btn()
        sort_driver.click_first_name_btn()
        sort_driver.check_names_list()

    @allure.title("Удалить пользователя с именем, "
                  "близким по длине к среднему имён всех клиентов")
    async def test_delete_customer(self, driver):
        del_driver = DeleteClient(driver)

        del_driver.open_target_page()
        del_driver.click_customers_btn()
        customer_id = del_driver.find_optimal_customer()
        del_codes = del_driver.get_deletion_customer_code(customer_id)
        del_driver.delete_customer(customer_id)
        del_driver.check_successful_deletion(del_codes)


@allure.suite("Набор API-тестов")
class TestsAPI:
    @allure.title("Получить данные об объекте по ID")
    def test_get_data_by_id(self):
        get_id = GetAPI()
        entry = get_id.get_by_id("2")
        assert entry.title is not None and entry.entry_id == 2, (
            "[ERROR] Данные не совпадают или не поля не заполнены"
        )

    @allure.step("Получить данные обо всех объектах")
    def test_get_all_data(self):
        get_id = GetAPI()
        entries = get_id.get_all()
        for entry in entries:
            assert entry.title is not None, (
                "[ERROR] Данные не совпадают или не поля не заполнены"
            )

    @allure.step("Создать новый объект")
    def test_create_new_data(self):
        create_id = PostAPI()
        return create_id.create_data("Watermelon")

    @allure.step("Удалить объект по id")
    def test_del_data_by_id(self):
        del_id = DelAPI()
        entry_id = self.test_create_new_data()
        del_id.del_by_id(entry_id)

    @allure.title("Изменить объект по id")
    def test_edit_data_by_id(self):
        patch_id = PatchAPI()
        patch_id.patch_data(self.test_create_new_data(), "Pineapple", True)
