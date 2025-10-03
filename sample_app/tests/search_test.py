from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000")

# Login first
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

time.sleep(2)
search_box = driver.find_element(By.NAME, "query")
search_box.send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

time.sleep(2)
assert "Search Results for \"selenium\"" in driver.page_source
print("Search test passed.")
driver.quit()