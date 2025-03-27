import allure
import pytest

from Pages.AddClient.AddClient import AddClient
from Pages.DeleteClient.DeleteClient import DeleteClient
from Pages.SortClients.SortClients import SortClients


@allure.suite("Набор тестов")
class Tests:
    @allure.title("Добавить клиента")
    @pytest.mark.asyncio
    async def test_add_customer(self, driver):
        customer_driver = AddClient(driver)

        customer_driver.open_target_page()
        code = customer_driver.generate_post_code()
        customer_driver.click_add_customer()
        customer_driver.fill_all_fields(code)
        customer_driver.confirm_adding()

    @allure.title("Сортировать пользователей по имени")
    @pytest.mark.asyncio
    async def test_sort_customers(self, driver):
        sort_driver = SortClients(driver)

        sort_driver.open_target_page()
        sort_driver.click_customers_btn()
        sort_driver.click_first_name_btn()
        is_sorted = sort_driver.check_names_list()
        with allure.step("Список отсортирован неверно. Повторение прошлых 2 шагов "
                         "для обновления сортировки"):
            if not is_sorted:
                sort_driver.click_first_name_btn()
                assert sort_driver.check_names_list() == True

    @allure.title("Удалить пользователя с именем, "
                  "близким по длине к среднему имён всех клиентов")
    @pytest.mark.asyncio
    async def test_delete_customer(self, driver):
        del_driver = DeleteClient(driver)

        del_driver.open_target_page()
        del_driver.click_customers_btn()
        customer_id = del_driver.find_optimal_customer()
        del_driver.delete_customer(customer_id)
