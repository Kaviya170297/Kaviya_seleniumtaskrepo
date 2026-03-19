
import time
import logging
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

User_name = driver.find_element(By.ID, "user-name")
User_name.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

button = driver.find_element(By.ID, "login-button")
button.click()
time.sleep(3)

#1.Get title:
title = driver.title
print("Title:", title)

#2. Get url:
current_url = driver.current_url
print("Current URL:", current_url)

#3.Extract page content:
# page_content = driver.page_source
visible_text = driver.find_element(By.TAG_NAME, "body").text       #to show page content in visible text
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(visible_text)

print("Page content saved successfully!")
time.sleep(3)
driver.quit()

#pytest test case:
@pytest.mark.positive
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    logging.info(driver.title)

    User_name = driver.find_element(By.ID, "user-name")
    User_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()
    time.sleep(2)
    assert "inventory" in driver.current_url
    driver.quit()

@pytest.mark.negative
def test_invalid_login():                    #negative test case
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    logging.info(driver.title)              #to print title in report using logging info in

    User_name = driver.find_element(By.ID, "user-name")
    User_name.send_keys("stand_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secr_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()
    time.sleep(2)

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text  #.text removes the text in this locator and stores in error variable
    assert "Epic sadface: Username and password do not match any user in this service" in error
    driver.quit()


