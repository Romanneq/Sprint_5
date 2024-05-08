from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
import time



class TestTransfer:


    def test_transfer_personal_account(self, driver):
# Вход в форму регистрации
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys('gorohovikroman8123@yandex.ru')
        driver.find_element(*MestoLocators.field_password_form_input).send_keys('1234567')
        driver.find_element(*MestoLocators.button_input_form_input).click()
# Ожидание отображения главной страницы сервиса через кнопку "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[2]//button[text()="Оформить заказ"]')))
#Gереход по клику на «Личный кабинет».
        driver.find_element(*MestoLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/p["В этом разделе вы можете изменить свои персональные данные"]')))
        time.sleep(1)