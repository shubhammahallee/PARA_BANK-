import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readConfig import ReadConfig

class TestLogin:

    # Test 1 — Valid Login
    def test_valid_login(self, setup):
        driver = setup
        driver.get(ReadConfig.getBaseUrl())

        lp = LoginPage(driver)
        lp.login(ReadConfig.getUsername(), ReadConfig.getPassword())

        assert "overview" in driver.current_url.lower(), "Login Failed ❌"
        print("Valid Login Passed ✅")

    # Test 2 — Invalid Login
    def test_invalid_login(self, setup):
        driver = setup
        driver.get(ReadConfig.getBaseUrl())

        lp = LoginPage(driver)
        lp.login("wronguser", "wrongpass")

        error = driver.find_element(
            By.XPATH,
            "//p[@class='error']"
        ).text

        assert "could not be verified" in error, "Error message nahi aaya ❌"
        print("Invalid Login Test Passed ✅")
