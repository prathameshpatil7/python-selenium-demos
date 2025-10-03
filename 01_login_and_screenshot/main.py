from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


try:
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(4)

    driver.save_screenshot("01_login_and_screenshot/login_success_screenshot.png")

finally:
    driver.quit()