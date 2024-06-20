import pytest
from selenium import webdriver
def test_open_url_verification():
    driver=webdriver.Chrome()
    driver.get("http://google.com")
    print(driver.title)