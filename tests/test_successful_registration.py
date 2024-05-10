from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import WebDriverWaitLocators



class TestRegistration:


    def test_successful_registration(self, driver, registration):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(WebDriverWaitLocators.input_form))
        text_display = driver.find_element(*WebDriverWaitLocators.input_form)
        assert text_display.is_displayed()