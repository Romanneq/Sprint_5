import pytest
from selenium import webdriver
from locators import MestoLocators
from helpers import get_registration_data


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get('https://stellarburgers.nomoreparties.site/')

    yield chrome

    chrome.quit()


@pytest.fixture
def registration(driver):
    name, email, password = get_registration_data()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*MestoLocators.field_name_form_register).send_keys(name)
    driver.find_element(*MestoLocators.field_email_form_register).send_keys(email)
    driver.find_element(*MestoLocators.field_password_form_register).send_keys(password)
    driver.find_element(*MestoLocators.button_register_form_register).click()
    return name, email, password