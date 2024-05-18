from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
from locators import WebDriverWaitLocators



class TestTransitionConstructorAndLogo:


    def test_transition_button_constructor_and_logo_service_from_personal_account(self, driver):
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
# Клик по кнопке "Конструктор"
        driver.find_element(*MestoLocators.button_constructor).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.text_assemble_burger))
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
# Клик по логотипу сервиса
        driver.find_element(*MestoLocators.button_constructor).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.text_assemble_burger))
        display_text_assemble_burger = driver.find_element(*WebDriverWaitLocators.text_assemble_burger)
        assert display_text_assemble_burger.is_displayed()
