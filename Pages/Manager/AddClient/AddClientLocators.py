from selenium.webdriver.common.by import By


class AddClientLocators:
    page_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    customer_btn = (By.XPATH, '//*[@class="btn btn-lg tab"][1]')
    post_code_field = (By.XPATH, '//*[@ng-model="postCd"]')
    first_name_field = (By.XPATH, '//*[@ng-model="fName"]')
    last_name_field = (By.XPATH, '//*[@ng-model="lName"]')
    confirm_btn = (By.XPATH, '//*[@type="submit"]')
    customers_btn = (By.XPATH, f'//*[@ng-class="btnClass3"]')

    @staticmethod
    def new_customer_name(customer_name: str):
        return By.XPATH, f'//*[@class="ng-binding"][1][text()="{customer_name}"]'

    @staticmethod
    def new_customer_surname(customer_surname: str):
        return By.XPATH, f'//*[@class="ng-binding"][2][text()="{customer_surname}"]'

    @staticmethod
    def new_customer_code(customer_id: str):
        return By.XPATH, f'//*[@class="ng-binding"][3][text()="{customer_id}"]'

    @staticmethod
    def delete_new_customer(code: str):
        return By.XPATH, f'//*[text()="{code}"]/..//*[text()="Delete"]'

    @staticmethod
    def get_deleted_customer_locator(code: str):
        return By.XPATH, f'//*[text()="{code}"]'
