from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestRegistration:
    def test_login_in_personal_account(self, driver):
        driver.get(Data.STELLAR_BURGERS_URL)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        personal_account = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PROFILE))
        assert personal_account.is_displayed()

    def test_login_in_constructor_from_personal_account(self, driver):
        driver.get(Data.STELLAR_BURGERS_URL)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        constructor_page = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()

    def test_logout_of_personal_account(self, driver):
        driver.get(Data.STELLAR_BURGERS_URL)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON)).click()
        successful_logout = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        assert successful_logout.is_displayed()