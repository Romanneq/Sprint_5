from selenium.webdriver.common.by import By
class MestoLocators:
    button_personal_account = (By.XPATH,'.//a[@class="AppHeader_header__link__3D_hX"]/p[text()="Личный Кабинет"]') # Локатор кнопки "Личный кабинет" в шапке страницы
    button_register_form_input = (By.LINK_TEXT, 'Зарегистрироваться') # локатор кнопки "Зарегистрироваться" в форме входа на страницу сервиса
    field_name_form_register = (By.XPATH, './/fieldset[1]/div/div/input') # локатор поля Имя в форме регистрации пользователя
    field_email_form_register = (By.XPATH, './/fieldset[2]/div/div/input') # локатор поля Email в форме регистрации пользователя
    field_password_form_register = (By.NAME, "Пароль") # локатор поля Пароль в форме регистрации пользователя
    button_register_form_register = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # локатор кнопки "Зарегистрироваться в форме регистрации пользователя
    button_log_on_main_page = (By.XPATH, ".//section[2]//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # локатор кнопки "Войти в аккаунт" на главной странице сервиса
    field_email_form_input = (By.XPATH, ".//fieldset[1]/div/div/input") # локатор поля email в форме входа в сервис
    field_password_form_input = (By.XPATH, './/fieldset[2]/div/div/input') # локатор поля password в форме входа в сервис
    button_input_form_input = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # локатор кнопки "войти" в форме входа в сервис
    button_exit_in_personal_account = (By.XPATH, './/li[3]/button[text()="Выход"]') # локатор кнопки "Выход" в личном кабинете
    button_input_form_register = (By.XPATH, ".//a[text()='Войти']") # локатор кнопки "Войти" в форме регистрации
    button_input_recovery_form = (By.XPATH, ".//p[2]/a[@class='Auth_link__1fOlj']") # локатор кнопки "Восстановление пароля"
    button_input_reverse_recovery_form = (By.XPATH, ".//a[text()='Войти']") # локатор кнопки "Войти" в форме восстановление пароля
    button_constructor = (By.XPATH, ".//li[1]/a[@class='AppHeader_header__link__3D_hX']") # локатор кнопки "Конструктор" в шапке страницы сервиса
    logo_service = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # локатор логотипа сервиса
    section_sauces = (By.XPATH,".//section[1]/div[1]/div[2][@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']") # локатор раздела "Соусы" на главной странице сервиса
    section_rolls = (By.XPATH,".//section[1]/div[1]/div[1]/span[text()='Булки']") # локатор раздела "Булки" на главной странице сервиса
    sections_fillings = (By.XPATH,".//section[1]/div[1]/div[3]/span[text()='Начинки']") # локатор раздела "Начинки" на главной странице сервиса