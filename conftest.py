import pytest
from selenium import webdriver
from utilities.readConfig import ReadConfig

@pytest.fixture()
def setup():
    browser = ReadConfig.getBrowser()
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    
    driver.maximize_window()
    yield driver
    driver.quit()
