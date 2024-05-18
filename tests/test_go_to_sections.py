from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MestoLocators



class TestTransferSections:


    def test_go_to_sections_rolls(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.section_rolls))
        driver.find_element(*MestoLocators.section_sauces).click()
        # Переход к разделу булки
        driver.find_element(*MestoLocators.section_rolls).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.section_rolls))
        display_rolls = driver.find_element(*MestoLocators.section_rolls)
        assert display_rolls.is_displayed()


    def test_go_to_sections_sauces(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.section_rolls))
        # Переход к разделу соусы
        driver.find_element(*MestoLocators.section_sauces).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.section_sauces))
        display_sauces = driver.find_element(*MestoLocators.section_sauces)
        assert display_sauces.is_displayed()


    def test_go_to_sections_fillings(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.section_rolls))
#Переход к разделу начинки
        driver.find_element(*MestoLocators.sections_fillings).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MestoLocators.sections_fillings))
        display_fillings = driver.find_element(*MestoLocators.sections_fillings)
        assert display_fillings.is_displayed()