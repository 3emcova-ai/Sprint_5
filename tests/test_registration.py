from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Data.STELLAR_BURGERS_URL)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_FIELD)).send_keys(Data.NAME)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Data.email_generation())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        login_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    #def test_invalid_password_error(self, driver):
             