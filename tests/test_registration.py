from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestRegistration:
    def test_successful_registration(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_FIELD)).send_keys(Data.NAME)
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Data.email_generation())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        
    def test_invalid_password_error(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_FIELD)).send_keys(Data.NAME)
        driver.find_element(*Locators.LOG_EMAIL_FIELD).send_keys(Data.email_generation())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD_INVALID)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_INVALID_PASSWORD))
   