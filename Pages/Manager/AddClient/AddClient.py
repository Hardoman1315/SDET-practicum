import allure
from selenium.webdriver.common.alert import Alert

from Helpers.BasePage import BasePage
from Helpers.StringManipulator import StringManipulator
from Pages.Manager.AddClient.AddClientLocators import AddClientLocators
from data.lines import add_customer, customers, first_name, last_name, post_code


class AddClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    str_manipulator = StringManipulator()

    @allure.step("Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(AddClientLocators.page_url)

    @allure.step(f"Нажать кнопку '{add_customer}'")
    def click_add_customer(self) -> None:
        self.click_element(AddClientLocators.customer_btn)

    @allure.step(f"Ввести код в поле {post_code}")
    def insert_postcode(self, code: str) -> None:
        code = str(code)
        self.insert_value(AddClientLocators.post_code_field, code)

    @allure.step(f"Ввести имя в поле {first_name}")
    def insert_first_name(self, code: str) -> None:
        self.insert_value(AddClientLocators.first_name_field, self.str_manipulator.extract_name_from_code(code))

    @allure.step(f"Ввести фамилию в поле {last_name}")
    def insert_last_name(self, code: str) -> None:
        self.insert_value(AddClientLocators.last_name_field, self.str_manipulator.extract_surname_from_code(code))

    @allure.step("Заполнить все поля")
    def fill_all_fields(self, code: str) -> None:
        self.insert_first_name(code)
        self.insert_last_name(code)
        self.insert_postcode(code)

    @allure.step(f"Нажать кнопку подтверждения '{add_customer}'")
    def confirm_adding(self):
        self.click_element(AddClientLocators.confirm_btn)

    @allure.step("Закрыть всплывающее уведомление")
    def close_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    @allure.step(f"Нажать кнопку '{customers}'")
    def click_customers_btn(self) -> None:
        self.click_element(AddClientLocators.customers_btn)

    @allure.step("Проверить существование нового пользователя")
    def check_new_customer_existence(self, code: str) -> None:
        """
        This method search for user with name, surname and post-code, which were used to create him.
        :param code: Created user post-code
        :return: None
        """
        self.find_element(AddClientLocators.new_customer_name(
            self.str_manipulator.extract_name_from_code(code)))

        self.find_element(AddClientLocators.new_customer_surname(
            self.str_manipulator.extract_surname_from_code(code)))

        self.find_element(AddClientLocators.new_customer_code(code))

    def clear_test_entities(self, code: str) -> None:
        self.delete_new_customer(code)
        self.check_successful_deletion(code)

    def delete_new_customer(self, code: str) -> None:
        self.click_element(AddClientLocators.delete_new_customer(code))

    def check_successful_deletion(self, code: str) -> None:
        """
        Check if there still left user which were supposed to be deleted.
        :param code: Deleted user post-code
        :return: None
        """
        matches = []
        matches.extend(self.check_presence_of_element(
            AddClientLocators.get_deleted_customer_locator(code)))
        assert matches == [], (
            "[ERROR] Один или несколько пользователей не было удалено"
        )
