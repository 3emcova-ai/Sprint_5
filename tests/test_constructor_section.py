import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


class TestConstructorSection:
    def test_section_buns(self, driver, authorization):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TOPPINGS_BUTTON)).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUNS_SECTION))
        
    @pytest.mark.parametrize('button_locator, section_locator', [(Locators.SAUCES_BUTTON, Locators.SAUCES_SECTION), (Locators.TOPPINGS_BUTTON, Locators.TOPPINGS_SECTION)])
    def test_section_activation(self, driver, authorization, button_locator, section_locator):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(button_locator)).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(section_locator))
