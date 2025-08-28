from selenium import webdriver
import pytest

def setup():
    driver = webdriver.Chrome(options = webdriver.ChromeOptions())
    return driver

