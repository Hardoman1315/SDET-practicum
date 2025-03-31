from selenium.webdriver.common.by import By


class DeleteClientLocators:
    page_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    customers_btn = (By.XPATH, '//*[@ng-class="btnClass3"]')
    customers_list = (By.XPATH, '//*[contains(@ng-repeat, "cust in")]//*[@class="ng-binding"][1]')

    @staticmethod
    def customer_name(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]//*[@class="ng-binding"][1]'

    @staticmethod
    def delete_customer_btn(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]//*[@ng-click="deleteCust(cust)"]'

    @staticmethod
    def get_customer_code(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]/./*[@class="ng-binding"][3]'

    @staticmethod
    def get_deleted_customer_locator(code: str):
        return By.XPATH, f'//*[text()="{code}"]'
