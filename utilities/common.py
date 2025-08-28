import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.ReadProperties import ReadConfig
from PageObjects.LoginPage import LoginPage
from TestCases.conftest import setup


class CommonUtils:
    @staticmethod
    def perform_login(driver=None):
        """
        Performs login and returns the driver instance
        If driver is not provided, creates a new one
        """
        if driver is None:
            driver = setup()

        baseUrl = ReadConfig.getApplicationURL()
        username = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()

        driver.get(baseUrl)
        lp = LoginPage(driver)
        time.sleep(5)
        lp.setemail(username)
        lp.setpassword(password)
        lp.clicklogin()

        return driver

    @staticmethod
    def login_and_verify():
        """
        Performs login and verifies successful login
        Returns driver instance if successful, None if failed
        """
        driver = CommonUtils.perform_login()

        # Add explicit wait for login verification
        wait = WebDriverWait(driver, 10)

        try:
            # Wait for page to load after login
            wait.until(lambda d: d.title == "Astrom HQ")
            print("Login successful - page title verified")
            return driver
        except Exception as e:
            print(f"Login verification failed: {e}")
            driver.save_screenshot("Screenshots/login_failed.png")
            driver.close()
            return None

    @staticmethod
    def wait_for_element_clickable(driver, locator_type, locator_value, timeout=10):
        """
        Wait for element to be clickable
        """
        wait = WebDriverWait(driver, timeout)
        if locator_type.lower() == "id":
            return wait.until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif locator_type.lower() == "xpath":
            return wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")
