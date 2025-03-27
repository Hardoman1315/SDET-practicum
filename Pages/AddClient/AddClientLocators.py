from selenium.webdriver.common.by import By


class AddClientLocators:
    page_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    customer_btn = (By.XPATH, '//*[@class="btn btn-lg tab"][1]')
    post_code_field = (By.XPATH, '//*[@ng-model="postCd"]')
    first_name_field = (By.XPATH, '//*[@ng-model="fName"]')
    last_name_field = (By.XPATH, '//*[@ng-model="lName"]')
    confirm_btn = (By.XPATH, '//*[@type="submit"]')
