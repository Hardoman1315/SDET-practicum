from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, timeout = 60):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url: str) -> None:
        self.driver.get(url)

    def find_element(self, locator: WebDriver or tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, 60).until(
            ec.presence_of_element_located(locator)
        )

    def find_elements(self, locator: WebDriver or tuple[str, str]) -> list[WebElement]:
        return WebDriverWait(self.driver, 60).until(
            ec.presence_of_all_elements_located(locator)
        )

    def get_element_text(self, locator: WebDriver or tuple[str, str]) -> str:
        return self.find_element(locator).text

    def click_element(self, locator: WebDriver or tuple[str, str]) -> None:
        return self.find_element(locator).click()

    def insert_value(self, locator: WebDriver or tuple[str, str], value: str) -> None:
        return self.find_element(locator).send_keys(value)
