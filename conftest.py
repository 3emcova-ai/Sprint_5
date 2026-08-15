import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    #print("🚀 Закрываю браузер")
    #driver.quit()
