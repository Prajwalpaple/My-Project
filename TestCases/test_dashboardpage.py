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
from PageObjects.DashboardPage import DashboardPage


class Test_002_Dashboard:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    def test_ManageRgdUserbtn(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.click_manage_regd_users()
        print("current url: ",self.driver.current_url)
        time.sleep(5)
        expected_url = 'https://astrom-dev.ascend.com.sa/operations/user-management'
        act_url = self.driver.current_url
        print(act_url)
        if expected_url == act_url :
            assert True
        else:
            assert False
        self.driver.close()
    
    def test_ManageRoles(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.click_manage_roles()
        time.sleep(5)
        expected_url = 'https://astrom-dev.ascend.com.sa/operations/roles-management'
        act_url_1 = self.driver.current_url
        print(act_url_1)
        if expected_url == act_url_1 :
            assert True
        else:
            assert False
        self.driver.close()

    def test_ManageBed(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.click_manage_bed
        time.sleep(5)
        expected_url = 'https://astrom-dev.ascend.com.sa/clinical-operations/occupancy-manager'
        act_url_2 = self.driver.current_url
        print(act_url_2)
        if expected_url == act_url_2 :
            assert True
        else:
            assert False
        self.driver.close()

    def test_ManageImaging(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.click_manage_imagingmodules
        time.sleep(5)
        expected_url = 'https://astrom-dev.ascend.com.sa/imaging-manager/modality-queue'
        act_url_3 = self.driver.current_url
        print(act_url_3)
        if expected_url == act_url_3 :
            assert True
        else:
            assert False
        self.driver.close()

    def test_ManageStaffingandWorkforce(self):
        self.driver = setup()
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setemail(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.click_manage_staff_workforce
        time.sleep(5)
        expected_url = 'https://astrom-dev.ascend.com.sa/staffing-and-workforce/nurse-load-status'
        act_url_3 = self.driver.current_url
        print(act_url_3)
        if expected_url == act_url_3 :
            assert True
        else:
            assert False
        self.driver.close()


        
