from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators



class TestTransfer:


    def test_transfer_personal_account(self, driver, registration):
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
# Переход по клику на «Личный кабинет».
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.text_personal_account))
        display_text_in_personal_account = driver.find_element(*WebDriverWaitLocators.text_personal_account)
        assert display_text_in_personal_account.is_displayed()
