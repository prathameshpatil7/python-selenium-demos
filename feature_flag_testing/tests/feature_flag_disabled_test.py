from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000/")
    time.sleep(2)
    old_ui_element = driver.find_elements(By.ID, "old-ui-banner")
    assert len(old_ui_element) > 0, "Old UI banner not found when feature flag is disabled."
    print("Feature flag disabled test passed.")
finally:
    driver.quit()