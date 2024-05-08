from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
import time
from data import get_registration_data



class TestError:


    def test_error_authorization_incorrect_password(self, driver):
        email,password = get_registration_data()
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*MestoLocators.button_register_form_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))
    # регистрация
        driver.find_element(*MestoLocators.field_name_form_register).send_keys('Roman')
        driver.find_element(*MestoLocators.field_email_form_register).send_keys(email)
        driver.find_element(*MestoLocators.field_password_form_register).send_keys(len(password))
        driver.find_element(*MestoLocators.button_register_form_register).click()
    # ожидание отображения ошибки: Некорректный пароль
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/fieldset[3]//p[text()="Некорректный пароль"]')))
        time.sleep(2)