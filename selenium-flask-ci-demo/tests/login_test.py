from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000")

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

time.sleep(2)
assert "Dashboard" in driver.page_source
print("Login test passed.")
driver.quit()