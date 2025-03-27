if exist allure-results rmdir /s /q allure-results
pytest -n 3 --alluredir allure-results
allure serve allure-results
