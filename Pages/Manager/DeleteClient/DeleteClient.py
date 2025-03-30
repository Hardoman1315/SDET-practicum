import allure

from Helpers.BasePage import BasePage
from Pages.Manager.DeleteClient.DeleteClientLocators import DeleteClientLocators
from data.lines import customers, post_code


class DeleteClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(DeleteClientLocators.page_url)

    @allure.step(f"Нажать кнопку '{customers}'")
    def click_customers_btn(self) -> None:
        self.click_element(DeleteClientLocators.customers_btn)

    @allure.step("Получить список имён пользователей")
    def get_names_list(self) -> list[str]:
        """
        Getting list of users name.
        :return: list[str]
        """
        names = []
        for i in range(1, len(self.find_elements(DeleteClientLocators.customers_list)) + 1):
            names.append(self.get_element_text(DeleteClientLocators.customer_name(i)))
        return names

    @allure.step("Узнать длину каждого имени")
    def get_names_len(self) -> list[int]:
        """
        Count length of names from the list.
        :return: list[int]
        """
        names = self.get_names_list()
        names_len = [0] * len(names)
        for i in range(0, len(names)):
            names_len[i] = len(names[i])
        return names_len

    @allure.step("Посчитать среднюю длину имени")
    def calc_avg_len(self) -> float:
        """
        This method calculate average length of name among all the users
        :return: float
        """
        names_len = self.get_names_len()
        length = sum(names_len)
        return length / len(names_len)

    @allure.step("Найти пользователя с максимальном близким количеством символов в имени")
    def find_optimal_customer(self) -> list[int]:
        """
        This method search for users, which names length is closest to the
        average length and return they index.
        :return: list[int]
        """
        names_len = self.get_names_len()
        avg_len = self.calc_avg_len()
        diff_list = [0.0] * len(names_len)
        for i in range(0, len(names_len)):
            diff_list[i] = (abs(avg_len - names_len[i]))
        min_value = min(diff_list)
        return [i for i, x in enumerate(diff_list) if x == min_value]

    @allure.step(f"Получить {post_code} удаляемых пользователей")
    def get_deletion_customer_code(self, customer_id: list[str]):
        """
        This method save post-codes of users for deletion
        :param customer_id: index of users for deletion
        :return: list[str]
        """
        codes_list = [''] * len(customer_id)
        for i in range(0, len(customer_id), 1):
            codes_list[i] = self.get_element_text(DeleteClientLocators.get_customer_code(customer_id[i]))
        return codes_list

    @allure.step("Удалить пользователя с максимальном близким количеством символов в имени")
    def delete_customer(self, customer_id: list[int]) -> None:
        """
        This method deleting users with successful condition by they index.
        :param customer_id: index of users for deletion
        :return: None
        """
        for i in range(len(customer_id) - 1, -1, -1):
            self.click_element(DeleteClientLocators.delete_customer_btn(customer_id[i]))

    @allure.step("Проверить успешное удаление пользователя")
    def check_successful_deletion(self, customer_codes: list[str]):
        """
        Check if there still left users which were supposed to be deleted.
        :param customer_codes: Deleted user post-code
        :return: None
        """
        matches = []
        for i in range(0, len(customer_codes), 1):
            matches.extend(self.check_presence_of_element(
                DeleteClientLocators.get_deleted_customer_locator(customer_codes[i])))
        assert matches == [], (
            "[ERROR] Один или несколько пользователей не было удалено"
        )
