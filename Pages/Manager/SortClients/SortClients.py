import allure

from Helpers.BasePage import BasePage
from Pages.Manager.SortClients.SortClientsLocators import SortClientLocators
from data.lines import customers, first_name


class SortClients(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(SortClientLocators.page_url)

    @allure.step(f"Нажать кнопку '{customers}'")
    def click_customers_btn(self) -> None:
        self.click_element(SortClientLocators.customers_btn)

    @allure.step(f"Нажать кнопку '{first_name}'")
    def click_first_name_btn(self) -> None:
        self.click_element(SortClientLocators.first_name_btn)

    @allure.step("Получить список имён пользователей")
    def get_customer_names(self) -> list[str]:
        names = []
        for i in range(1, len(self.find_elements(SortClientLocators.customers_list)) + 1):
            names.append(self.get_element_text(SortClientLocators.customer_name(i)))
        return names

    @allure.step("Сортировать имена в алфавитном порядке")
    def sort_names(self) -> list[str]:
        names = self.get_customer_names()
        return sorted(names)

    @allure.step("Сравнить отсортированный список с оригинальным")
    def check_names_list(self) -> None:
        assert self.get_customer_names() == self.sort_names(), (
            '[FAILED] Список имён не отсортирован в алфавитном порядке'
        )
