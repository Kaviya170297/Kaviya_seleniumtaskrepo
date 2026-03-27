
import time
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#webdriver setup:
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
# test_login.py

from selenium.webdriver.common.by import By

BASE_URL = "https://www.guvi.in/"
LOGIN_URL = "https://www.guvi.in/sign-in/"

#url navigation check:
def test_login_url_navigation(setup):
    driver = setup
    driver.get(BASE_URL)
    driver.find_element(By.ID, "login-btn").click()
    driver.quit()

#To check fields are visible:
def test_input_fields_visible_enabled(setup):
    driver = setup
    driver.get(LOGIN_URL)

    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    assert username.is_displayed() and username.is_enabled()
    assert password.is_displayed() and password.is_enabled()
    driver.quit()

#To check Valid login:
def test_valid_login(setup):
    driver = setup
    driver.get(LOGIN_URL)

    driver.find_element(By.ID, "email").send_keys("kaviyasubramani8181@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Batch@107")
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)
    driver.quit()

#To check inValid login and errors:
def test_invalid_login(setup):
    driver = setup
    driver.get("https://www.guvi.in/sign-in/")

    driver.find_element(By.ID, "email").send_keys("kaviya@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Batc107")
    driver.find_element(By.ID, "login-btn").click()
    wait = WebDriverWait(driver, 10)
    error = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "invalid-feedback"))
    )

    assert "Incorrect Email or Password" in error.text

#To check empty submit:
def test_empty_login(setup):
    driver = setup
    driver.get(LOGIN_URL)

    driver.find_element(By.ID, "login-btn").click()
    errors = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
    assert len(errors) > 0

    driver.quit()
