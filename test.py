import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_index_page(browser):
    browser.get("http://localhost/index.html")
    register_link = browser.find_element(By.LINK_TEXT, "Register")
    register_link.click()

def test_index_page2(browser):
    browser.get("http://localhost/index.html")
    register_link = browser.find_element(By.LINK_TEXT, "Login")
    register_link.click()


def test_index_page3(browser):
    browser.get("http://localhost/index.html")
    register_link = browser.find_element(By.LINK_TEXT, "CATALOGUE")
    register_link.click()
    assert browser.current_url == "http://localhost/category.html"


def test_index_page4(browser):
    browser.get("http://localhost/category.html")
    register_link2 = browser.find_element(By.LINK_TEXT, "0 items in cart")
    register_link2.click()
    assert browser.current_url == "http://localhost/basket.html"

def test_index_page5(browser):
    browser.get("http://localhost/basket.html")
    register_link2 = browser.find_element(By.LINK_TEXT, "Continue shopping")
    register_link2.click()
    assert browser.current_url == "http://localhost/category.html"

def test_index_page6(browser):
    browser.get("http://localhost/category.html")
    register_link2 = browser.find_element(By.LINK_TEXT, "Add to cart")
    register_link2.click()
    assert browser.current_url == "http://localhost/category.html#"