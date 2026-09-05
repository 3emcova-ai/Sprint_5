from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestLogin:
    def test_login_button_on_main_page(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
 
    def test_login_button_in_personal_account(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_login_button_in_registration_form(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        
    def test_login_button_in_password_recovery_page(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PASSWORD_RECOVERY_LINK)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_LINK)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
      