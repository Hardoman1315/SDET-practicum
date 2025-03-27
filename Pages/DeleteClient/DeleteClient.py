import allure

from Helpers.BasePage import BasePage
from Pages.DeleteClient.DeleteClientLocators import DeleteClientLocators
from data.lines import customers


class DeleteClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    @allure.step(f"Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(DeleteClientLocators.page_url)

    @allure.step(f"Нажать кнопку '{customers}'")
    def click_customers_btn(self) -> None:
        self.click_element(DeleteClientLocators.customers_btn)

    @allure.step(f"Получить список имён пользователей")
    def get_names_list(self) -> list[str]:
        names = []
        for i in range(1, len(self.find_elements(DeleteClientLocators.customers_list)) + 1):
            names.append(self.get_element_text(DeleteClientLocators.customer_name(i)))
        return names

    @allure.step(f"Узнать длину каждого имени")
    def get_names_len(self) -> list[int]:
        names = self.get_names_list()
        names_len = [0] * len(names)
        for i in range(0, len(names)):
            names_len[i] = len(names[i])
        return names_len

    @allure.step(f"Посчитать среднюю длину имени")
    def calc_avg_len(self) -> float:
        names_len = self.get_names_len()
        length = sum(names_len)
        return length / len(names_len)

    @allure.step(f"Найти пользователя с максимальном близким количеством символов в имени")
    def find_optimal_customer(self) -> list[int]:
        names_len = self.get_names_len()
        avg_len = self.calc_avg_len()
        diff_list = [0.0] * len(names_len)
        for i in range(0, len(names_len)):
            diff_list[i] = (abs(avg_len - names_len[i]))
        min_value = min(diff_list)
        return [i for i, x in enumerate(diff_list) if x == min_value]

    @allure.step(f"Удалить пользователя с максимальном близким количеством символов в имени")
    def delete_customer(self, customer_id: list[int]) -> None:
        for i in range(len(customer_id) - 1, -1, -1):
            self.click_element(DeleteClientLocators.delete_customer_btn(customer_id[i]))
