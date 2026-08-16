import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.STELLAR_BURGERS_URL)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def authorization(driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOG_EMAIL_FIELD)).send_keys(Data.REGISTERED_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
