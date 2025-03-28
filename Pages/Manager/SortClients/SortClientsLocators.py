from selenium.webdriver.common.by import By


class SortClientLocators:
    page_url = f'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    customers_btn = (By.XPATH, f'//*[@ng-class="btnClass3"]')
    customers_list = (By.XPATH, f'//*[contains(@ng-repeat, "cust in")]//*[@class="ng-binding"][1]')
    first_name_btn = (By.XPATH, f'//*[contains(@ng-click, "sortType = \'fName\'")]')

    @staticmethod
    def customer_name(customer_id: int):
        return By.XPATH, f'//*[contains(@ng-repeat, "cust in")][{customer_id}]//*[@class="ng-binding"][1]'
