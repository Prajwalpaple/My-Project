from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait



class LoginPage:
    user_Name = "email"
    password_Name = "password"
    clicklogin_ID = "sign-in"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self,username):
        self.driver.find_element(By.NAME, self.user_Name).clear()
        self.driver.find_element(By.NAME, self.user_Name).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.NAME, self.password_Name).clear()
        self.driver.find_element(By.NAME, self.password_Name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.ID, self.clicklogin_ID).click()