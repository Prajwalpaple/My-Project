from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait

class Patient_inboundPage:
    managebed_ID = 'manage-bed-&-discharge-operations'
    toggle_menu_xpath = '//*[@id="toggle-menu-button"]/svg'
    clinical_operations_xpath = '//*[@id="tree-hamburger-menu"]/div[2]/div/button/span'
    emergency_dept_xpath = '//*[@id="tree-hamburger-menu"]/div[2]/div/button[4]/span'
    patient_inbond_xpath = '//*[@id="tree-hamburger-menu"]/div[2]/div/button[5]/span/span'
    time_view_ID = 'time-view'


    def __init__(self, driver):
        self.driver = driver

    def click_manage_bed(self):
        self.driver.find_element(By.ID, self.managebed_ID).click()

    def click_toggle_menu(self):
        self.driver.find_element(By.XPATH, self.toggle_menu_xpath).click()

    def click_clinical_operations(self):
        self.driver.find_element(By.XPATH, self.clinical_operations_xpath).click()

    def click_emergency_dept(self):
        self.driver.find_element(By.XPATH, self.emergency_dept_xpath).click()

    def click_patient_inbond(self):
        self.driver.find_element(By.XPATH, self.patient_inbond_xpath).click()

    def click_time_view(self):
        self.driver.find_element(By.ID, self.time_view_ID).click()
