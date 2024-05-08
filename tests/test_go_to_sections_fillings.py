from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators
import time



class TestTransferSectionsFillings:


    def test_go_to_sections_fillings(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[1]/div[2]/h2[1][text()="Булки"]')))
#Переход к разделу начинки
        driver.find_element(*MestoLocators.sections_fillings).click()
        time.sleep(1)