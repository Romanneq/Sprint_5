from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
import time



class TestTransitionConstructorAndLogo:


    def test_transition_button_constructor_and_logo_service_from_personal_account(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
        time.sleep(1)
        driver.find_element(*MestoLocators.button_constructor).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[1]/h1[text()='Соберите бургер']")))
        time.sleep(1)
        driver.find_element(*MestoLocators.button_log_on_main_page).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        time.sleep(1)
#Клик по логотипу сервиса
        driver.find_element(*MestoLocators.button_constructor).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[1]/h1[text()='Соберите бургер']")))
        time.sleep(1)