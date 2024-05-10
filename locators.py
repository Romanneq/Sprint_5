from selenium.webdriver.common.by import By
class MestoLocators:
    button_personal_account = (By.XPATH,'.//a[@class="AppHeader_header__link__3D_hX"]/p[text()="Личный Кабинет"]') # Локатор кнопки "Личный кабинет" в шапке страницы
    button_register_form_input = (By.LINK_TEXT, 'Зарегистрироваться') # локатор кнопки "Зарегистрироваться" в форме входа на страницу сервиса
    field_name_form_register = (By.XPATH, ".//label[text()='Имя']/parent::div/input") # локатор поля Имя в форме регистрации пользователя
    field_email_form_register = (By.XPATH, ".//label[text()='Email']/parent::div/input") # локатор поля Email в форме регистрации пользователя
    field_password_form_register = (By.NAME, "Пароль") # локатор поля Пароль в форме регистрации пользователя
    button_register_form_register = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # локатор кнопки "Зарегистрироваться в форме регистрации пользователя
    button_log_on_main_page = (By.XPATH, ".//button[text()='Войти в аккаунт']") # локатор кнопки "Войти в аккаунт" на главной странице сервиса
    field_email_form_input = (By.NAME, "name") # локатор поля email в форме входа в сервис
    field_password_form_input = (By.NAME, 'Пароль') # локатор поля password в форме входа в сервис
    button_input_form_input = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # локатор кнопки "войти" в форме входа в сервис
    button_exit_in_personal_account = (By.XPATH, './/button[text()="Выход"]') # локатор кнопки "Выход" в личном кабинете
    button_input_form_register = (By.XPATH, ".//a[text()='Войти']") # локатор кнопки "Войти" в форме регистрации
    button_input_recovery_form = (By.XPATH, ".//a[text()='Восстановить пароль']") # локатор кнопки "Восстановление пароля"
    button_input_reverse_recovery_form = (By.XPATH, ".//a[text()='Войти']") # локатор кнопки "Войти" в форме восстановление пароля
    button_constructor = (By.XPATH, ".//p[text()='Конструктор']") # локатор кнопки "Конструктор" в шапке страницы сервиса
    logo_service = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # локатор логотипа сервиса
    section_sauces = (By.XPATH, ".//span[text()='Соусы']") # локатор раздела "Соусы" на главной странице сервиса
    section_rolls = (By.XPATH, ".//span[text()='Булки']") # локатор раздела "Булки" на главной странице сервиса
    sections_fillings = (By.XPATH, ".//span[text()='Начинки']") # локатор раздела "Начинки" на главной странице сервиса
class WebDriverWaitLocators:
    input_form = (By.XPATH, './/h2[text()="Вход"]') # локатор формы авторизации сервиса
    button_place_an_order = (By.XPATH, ".//button[text()='Оформить заказ']") # локатор кнопки "Оформить заказ" на главной странице сервиса
    register_form = (By.XPATH, './/h2[text()="Регистрация"]') # локатор формы регистрации
    error_display_incorrect_password = (By.XPATH, './/p[text()="Некорректный пароль"]') # локатор отображения ошибки "Неправильный пароль"
    recovery_form = (By.XPATH, './/h2[text()="Восстановление пароля"]') # локатор формы "Восстановление пароля"
    text_personal_account = (By.XPATH, './/p["В этом разделе вы можете изменить свои персональные данные"]') # локатор текста в личном кабинете
    text_assemble_burger = (By.XPATH, ".//h1[text()='Соберите бургер']") # локатор текста "Соберите бургер" на главной странице сервиса
