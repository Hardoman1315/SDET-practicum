import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')

    if os.getenv('CI_ENV') == 'true':
        options.add_argument("--headless=new")  # Включаем headless-режим только для CI/CD
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    _driver = webdriver.Chrome(options=options)
    _driver.minimize_window()
    yield _driver
    _driver.quit()
