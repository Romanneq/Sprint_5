from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators



class TestLogoutFromPersonalAccount:
    def test_log_out_button_from_personal_account(self, driver, registration):
        name, email, password = registration
# Вход в форму регистрации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
        driver.find_element(*MestoLocators.button_personal_account).click()
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys(email)
        driver.find_element(*MestoLocators.field_password_form_input).send_keys(password)
        driver.find_element(*MestoLocators.button_input_form_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.button_place_an_order))
# Вход в личный кабинет
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(MestoLocators.button_exit_in_personal_account))
# Проверка кнопки "Выход" из личного кабинета
        driver.find_element(*MestoLocators.button_exit_in_personal_account).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
        button_display = driver.find_element(*MestoLocators.button_input_form_input)
        assert button_display.is_displayed()