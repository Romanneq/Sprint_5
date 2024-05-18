# Проект автоматизации тестирования сервиса Stellar Burgers

1. Ссылка на сервис: "https://stellarburgers.nomoreparties.site/"
2. Основа для написания автотестов — фреймворк selenium.
3. Установить зависимости — pip install selenium, pip install pytest
4. Проверить, что selenium, pytest установлен: pip freeze
5. Команда для запуска — run
6. Описания локаторов – в файле locators.py
7. Автоматическая генерация name, email, password – в файле helpers.py
8. В файле conftest.py фикстуры: для запуска Chrome, регистрации пользователя на сайте сервиса 
7. Модуль data.py используется только в test_error_incorrect_password.py для ввода некорректного пароля