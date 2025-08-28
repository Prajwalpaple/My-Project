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


