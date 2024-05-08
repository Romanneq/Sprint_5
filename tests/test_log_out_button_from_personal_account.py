from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators



class TestLogoutFromPersonalAccount:
    def test_log_out_button_from_personal_account(self, driver):
# Вход в форму регистрации
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys('gorohovikroman8123@yandex.ru')
        driver.find_element(*MestoLocators.field_password_form_input).send_keys('1234567')
        driver.find_element(*MestoLocators.button_input_form_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[2]//button[text()="Оформить заказ"]')))
# Вход в личный кабинет
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/li[3]/button[text()="Выход"]')))
# Проверка кнопки "Выход" из личного кабинета
        driver.find_element(*MestoLocators.button_exit_in_personal_account).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))