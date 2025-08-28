import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.ReadProperties import ReadConfig
from PageObjects.LoginPage import LoginPage
from .conftest import setup
import time
import pytest
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_LoginpageTitle(self):
        self.logger.info("***********************TEST 001 STARTED*****************************")
        self.logger.info("***********************VERIFYING HOME PAGE TITLE ***************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        print("Actual title is: ", act_title)
        if act_title == "Astrom HQ":
            assert True
            self.logger.info("***********************HOMEPAGE TITLE TEST PASSED******************************")
            self.driver.close()
        else:
            self.logger.info("***********************HOMEPAGE TITLE TEST FAILED***************************")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginpagetitle.png")
            assert False

    def test_login(self):
        self.logger.info("***********************VERFYING THE LOGIN***************************")
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Astrom HQ":
            assert True
            self.logger.info("***********************LOGIN TEST PASSED***************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.info("***********************LOGIN TEST FALED***************************")
            assert False




