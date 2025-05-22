# Автоматизация тест-кейса для сайта "ОхотАктив"

## Описание
Автотест реализует сценарий регистрации/авторизации пользователя с валидной почтой через сайт https://ohotaktiv.ru/ и подтверждение кода из Gmail. Используется паттерн PageObject, Selenium, Pytest, Allure.

## Требования
- Python 3.10+
- Google Chrome (версия, совместимая с chromedriver)
- ChromeDriver (https://googlechromelabs.github.io/chrome-for-testing/#stable)
- pip
- Доступ к Gmail-аккаунту (email и пароль)

## Установка

2. Виртуальное окружение:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Зависимости:
   ```
   pip install -r requirements.txt
   ```

## Запуск

Запустите тест с параметрами:
   ```
   pytest --alluredir=allure-results -s --email <ваш_gmail> --password <ваш_пароль>
   ```

## Генерация и просмотр Allure-отчёта
1. Установите Allure Commandline: https://docs.qameta.io/allure/#_installing_a_commandline
2. Сгенерируйте и откройте отчёт:
   ```
   allure serve allure-results
   ```

## CI/CD (GitHub Actions)
- Workflow находится в `.github/workflows/python-app.yml`.
- Для запуска тестов в CI используйте секреты `TEST_EMAIL` и `TEST_PASSWORD`.
- После прогона тестов артефакт Allure-отчёта будет доступен для скачивания.

## Структура проекта
- `pages/` — PageObject-страницы и локаторы
- `test_OA_one.py` — основной автотест
- `screenshots/` — скриншоты ошибок (создаются автоматически)
- `allure-results/` — результаты для Allure-отчёта
- `.github/workflows/` — CI/CD pipeline

## Пример скриншота ошибки
![Пример скриншота ошибки](screenshots/fail_20250522_174936.png)

## Примечания
- Все параметры (email, password) передаются через командную строку или через секреты CI.
- Скриншоты ошибок сохраняются автоматически при падении теста.
- Для корректной работы с Gmail рекомендуется использовать отдельный тестовый аккаунт.

