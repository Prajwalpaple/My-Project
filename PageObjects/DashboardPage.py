from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    btnManageRgdUsers_ID = 'manage-registered-users'
    btnManageRoles_ID = 'manage-roles'
    btnManagebeddischargeOperation_ID = 'manage-bed-&-discharge-operations'

    def __init__(self, driver):
        self.driver = driver

    def click_manage_regd_users(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.btnManageRgdUsers_ID))).click()

    def click_manage_roles(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.btnManageRoles_ID))).click()

    def click_manage_bed(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.btnManagebeddischargeOperation_ID))).click()

