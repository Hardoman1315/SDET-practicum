cd ../.. || exit 1
[ -d allure-results ] && rm -rf allure-results
pytest -n 3 --alluredir allure-results
