from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestPersonalAccount:
    def test_login_in_personal_account(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE))
        
    def test_login_in_constructor_from_personal_account(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SECTION))

    def test_logout_of_personal_account(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON)).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
