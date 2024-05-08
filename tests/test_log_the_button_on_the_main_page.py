from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators



class TestButtonRegistration:

    def test_log_the_button_on_the_main_page(self, driver):
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys('gorohovikroman8123@yandex.ru')
        driver.find_element(*MestoLocators.field_password_form_input).send_keys('1234567')
        driver.find_element(By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидание отображения главной страницы сервиса через кнопку "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[2]//button[text()="Оформить заказ"]')))
