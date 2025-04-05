cd ../.. || exit 1
if [ -d allure-results ]; then
    allure serve allure-results
else
    ./generate_report.sh
fi
