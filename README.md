UI-автотесты для Stellar Burgers на Python + Selenium + pytest с Page Object Model,
кроссбраузерным запуском в Google Chrome и Mozilla Firefox и Allure-отчётом.
## Установка
python -m venv .venv
pip install -r requirements.txt
## Запуск всех тестов в Chrome и Firefox
pytest -v --alluredir=allure-results
Фикстура `driver` параметризована двумя браузерами, поэтому каждый тест выполняется
отдельно в Chrome и Firefox.
## Allure
Открыть отчёт:
allure serve allure-results
Сохранить статический HTML-отчёт:
allure generate allure-results -o allure-report --clean

