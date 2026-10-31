# Diplom_3 — UI-тестирование Stellar Burgers

## Технологии
- Python
- Selenium WebDriver
- Pytest
- Allure

## Структура проекта
- `pages/` — Page Object Model
- `locators/` — локаторы элементов
- `tests/` — автоматизированные тесты и фикстуры
- `helpers.py` — генерация тестовых данных
- `urls.py` — адреса приложения и API

## Проверяемая функциональность
- Переход между конструктором и лентой заказов
- Открытие и закрытие модального окна ингредиента
- Увеличение счётчика ингредиента
- Увеличение счётчиков заказов
- Отображение созданного заказа в разделе «В работе»

Тесты выполняются в Google Chrome и Mozilla Firefox.

## Установка зависимостей

pip install -r requirements.txt

## Запуск тестов

python -m pytest tests/ -v --alluredir=allure-results

## Генерация Allure-отчёта

allure generate allure-results -o allure-report --clean
