from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserManagement:
    user_management_ID = "manage-registered-users"
    name_filter_xpath = '//input[@placeholder="Enter Name"]'
    apply_click_xpath = '//button[text()="Apply"]'
    find_table_xpath = '//table[contains(@class, "caption-bottom")]'
    find_cell_xpath = './/tbody/tr'


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_user_management(self):  
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.user_management_ID)))
        self.driver.find_element(By.ID, self.user_management_ID).click()

    def click_name_filter(self, name = "Astrom"):
        self.driver.find_element(By.XPATH, self.name_filter_xpath).clear().sendkeys('astrom')
        self.driver.find_element(By.XPATH, self.name_filter_xpath).send_keys(name)

    def click_apply(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.apply_click_xpath))).click()

    def find_table(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.find_table_xpath)))

    def find_cell(self):
        self.driver.find_element(By.XPATH, self.find_cell_xpath).click()

