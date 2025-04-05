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
    def test_get_data_by_id(self, entry_id: str = "2", entry_title: str = None):
        get_id = GetAPI()
        entry = get_id.get_by_id(entry_id)
        if entry_title:
            with allure.step("Проверить что имя заполнено"):
                assert entry.title == entry_title, (
                    "[ERROR] Поле имени не заполнено"
                )
        else:
            with allure.step("Проверить что имя заполнено"):
                assert entry.title is not None, (
                    "[ERROR] Поле имени не заполнено"
                )

        with allure.step("Проверить что id запроса и ответа совпадают"):
            assert entry.entry_id == int(entry_id), (
                "[ERROR] id запроса и ответа не совпадают"
            )

    @allure.title("Получить данные обо всех объектах")
    def test_get_all_data(self):
        get_id = GetAPI()
        entries = get_id.get_all()
        with allure.step("Проверить что имя и id заполнены"):
            for entry in entries:
                assert entry.title is not None and entry.entry_id is not None, (
                    "[ERROR] Данные не совпадают или не поля не заполнены"
                )

    @allure.title("Создать новый объект")
    def test_create_new_data(self, fixture_delete, entry_title: str = "Watermelon"):
        create_id = PostAPI()
        response = create_id.create_data(entry_title)
        self.test_get_data_by_id(response, entry_title)
        fixture_delete.del_by_id(response)
        fixture_delete.check_del(response)

    @allure.title("Удалить объект по id")
    def test_del_data_by_id(self, fixture_post):
        del_id = DelAPI()
        entry_id = fixture_post.create_data("Dragonfruit")
        del_id.del_by_id(entry_id)
        with allure.step("Проверить успешное удаление объекта"):
            assert del_id.del_by_id(entry_id) == 500

    @allure.title("Изменить объект по id")
    def test_edit_data_by_id(self, fixture_delete, fixture_post, new_entry_title: str = "Pineapple"):
        patch_id = PatchAPI()
        entry_id = fixture_post.create_data("Dragonfruit")
        patch_id.patch_data(entry_id, new_entry_title, True)
        self.test_get_data_by_id(entry_id, new_entry_title)
        fixture_delete.del_by_id(entry_id)
