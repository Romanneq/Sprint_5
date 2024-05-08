from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators



class TestRegistration:


    def test_successful_registration(self, driver):
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*MestoLocators.button_register_form_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))
        driver.find_element(*MestoLocators.field_name_form_register).send_keys('Roman')
        driver.find_element(*MestoLocators.field_email_form_register).send_keys('gorohovikroman8123@yandex.ru')
        driver.find_element(*MestoLocators.field_password_form_register).send_keys('1234567')
        driver.find_element(*MestoLocators.button_register_form_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))