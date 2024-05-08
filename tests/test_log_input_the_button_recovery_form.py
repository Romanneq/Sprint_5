from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
import time



class TestInputFromRecoveryForm:


    def test_log_input_the_button_recovery_form(self, driver):
# Вход в форму регистрации
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
# Вход в форму "Восстановление пароля"
        driver.find_element(*MestoLocators.button_input_recovery_form).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Восстановление пароля"]')))
        time.sleep(1)
# Клик по кнопке "Войти" из формы Восстановление пароля
        driver.find_element(*MestoLocators.button_input_reverse_recovery_form).click()
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys('gorohovikroman8123@yandex.ru')
        driver.find_element(*MestoLocators.field_password_form_input).send_keys('1234567')
        driver.find_element(*MestoLocators.button_input_form_input).click()
# Ожидание отображения главной страницы сервиса через кнопку "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[2]//button[text()="Оформить заказ"]')))
        time.sleep(1)