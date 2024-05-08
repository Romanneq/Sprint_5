from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from locators import MestoLocators



class TestTransferSectionsRolls:
    def test_go_to_sections_rolls(self,driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[1]/div[2]/h2[1][text()="Булки"]')))
        driver.find_element(*MestoLocators.section_sauces).click()
        time.sleep(1)
#Переход к разделу булки
        driver.find_element(*MestoLocators.section_rolls).click()
        time.sleep(1)