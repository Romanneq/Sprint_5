from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators
from data import incorrect_password, name, email



class TestError:


    def test_error_authorization_incorrect_password(self, driver):
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.input_form))
        driver.find_element(*MestoLocators.button_register_form_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.register_form))
    # регистрация
        driver.find_element(*MestoLocators.field_name_form_register).send_keys(name)
        driver.find_element(*MestoLocators.field_email_form_register).send_keys(email)
        driver.find_element(*MestoLocators.field_password_form_register).send_keys(incorrect_password)
        driver.find_element(*MestoLocators.button_register_form_register).click()
    # ожидание отображения ошибки: Некорректный пароль
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.error_display_incorrect_password))
        display_incorrect_password = driver.find_element(*WebDriverWaitLocators.error_display_incorrect_password)
        assert display_incorrect_password.is_displayed()