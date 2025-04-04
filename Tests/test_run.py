import allure

from Helpers.Generator import Generator
from Pages.Manager.AddClient.AddClient import AddClient
from Pages.Manager.DeleteClient.DeleteClient import DeleteClient
from Pages.Manager.SortClients.SortClients import SortClients


@allure.suite("Набор тестов")
class Tests:
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
