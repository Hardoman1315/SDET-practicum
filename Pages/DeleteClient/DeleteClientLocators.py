from selenium.webdriver.common.by import By


class DeleteClientLocators:
    page_url = f'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    customers_btn = (By.XPATH, f'//*[@ng-class="btnClass3"]')
    customers_list = (By.XPATH, f'//*[contains(@ng-repeat, "cust in")]//*[@class="ng-binding"][1]')

    @staticmethod
    def customer_name(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]//*[@class="ng-binding"][1]'

    @staticmethod
    def delete_customer_btn(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]//*[@ng-click="deleteCust(cust)"]'
