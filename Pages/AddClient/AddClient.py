from random import randint

import allure

from Helpers.BasePage import BasePage
from Pages.AddClient.AddClientLocators import AddClientLocators
from data.lines import add_customer, post_code, first_name, last_name


class AddClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    @allure.step(f"Открыть целевую страницу")
    def open_target_page(self) -> None:
        self.open_page(AddClientLocators.page_url)

    @allure.step(f"Сгенерировать post-code")
    def generate_post_code(self) -> int:
        code = ""
        for i in range(10):
            code = code + str(randint(0, 100)).zfill(2)
        return int(code)

    @allure.step(f"Проверить что число не больше 25")
    def check_for_length(self, num: int) -> int:
        while num > 25:
            num = num - 25
        return num

    @allure.step(f"Извлечь имя из post-code")
    def extract_name_from_code(self, code: int) -> str:
        code = str(code)
        name_code = code[:10]
        name = f""
        for i in range(0, 9, 2):
            char_code = self.check_for_length(int(name_code[i:i + 2]))
            ucode = (char_code + 97)
            name = name + chr(ucode)
        return name

    @allure.step(f"Извлечь фамилию из post-code")
    def extract_surname_from_code(self, code: int) -> str:
        code = str(code)
        surname_code = code[10:]
        surname = f""
        for i in range(0, 9, 2):
            char_code = self.check_for_length(int(surname_code[i:i + 2]))
            ucode = (char_code + 97)
            surname = surname + chr(ucode)
        return surname

    @allure.step(f"Нажать кнопку '{add_customer}'")
    def click_add_customer(self) -> None:
        self.click_element(AddClientLocators.customer_btn)

    @allure.step(f"Ввести код в поле {post_code}")
    def insert_postcode(self, code: int) -> None:
        code = str(code)
        self.insert_value(AddClientLocators.post_code_field, code)

    @allure.step(f"Ввести имя в поле {first_name}")
    def insert_first_name(self, code: int) -> None:
        self.insert_value(AddClientLocators.first_name_field, self.extract_name_from_code(code))

    @allure.step(f"Ввести фамилию в поле {last_name}")
    def insert_last_name(self, code: int) -> None:
        self.insert_value(AddClientLocators.last_name_field, self.extract_surname_from_code(code))

    @allure.step(f"Заполнить все поля")
    def fill_all_fields(self, code: int) -> None:
        self.insert_first_name(code)
        self.insert_last_name(code)
        self.insert_postcode(code)

    @allure.step(f"Нажать кнопку подтверждения '{add_customer}'")
    def confirm_adding(self):
        self.click_element(AddClientLocators.confirm_btn)
