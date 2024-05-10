from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators



class TestButtonRegistrationOnMainPage:


    def test_log_the_button_on_the_main_page(self, driver, registration):
        name, email, password = registration
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.button_log_on_main_page))
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
# Вход в сервис
        driver.find_element(*MestoLocators.field_email_form_input).send_keys(email)
        driver.find_element(*MestoLocators.field_password_form_input).send_keys(password)
        driver.find_element(*MestoLocators.button_input_form_input).click()
# Ожидание отображения главной страницы сервиса через кнопку "Оформить заказ"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(WebDriverWaitLocators.button_place_an_order))
        display_button_place_an_order = driver.find_element(*WebDriverWaitLocators.button_place_an_order)
        assert display_button_place_an_order.is_displayed()
