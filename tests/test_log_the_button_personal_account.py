from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators


class TestButtonRegistrationPersonalAccount:


    def test_log_the_button_personal_account(self, driver, registration):
        name, email, password = registration
# Вход в форму регистрации
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
        driver.find_element(*MestoLocators.button_personal_account).click()
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys(email)
        driver.find_element(*MestoLocators.field_password_form_input).send_keys(password)
        driver.find_element(*MestoLocators.button_input_form_input).click()
# Ожидание отображения главной страницы сервиса через кнопку "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.button_place_an_order))
        display_button_place_an_order = driver.find_element(*WebDriverWaitLocators.button_place_an_order)
        assert display_button_place_an_order.is_displayed()