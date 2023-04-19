from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest
link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

@pytest.fixture()
def setup():
    browser = webdriver.Chrome()
    return browser

class Tests():

    def test_1(self, setup):
        setup.get(link)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first").send_keys(123)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second").send_keys(123)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third").send_keys(123)
        button = setup.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = setup.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered" == welcome_text
    def test_2(self, setup):
        setup.get(link2)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first").send_keys(123)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second").send_keys(123)
        setup.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third").send_keys(123)
        button = setup.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = setup.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
