from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000/?feature=new-ui")
    time.sleep(2)
    new_ui_element = driver.find_elements(By.ID, "new-ui-banner")
    assert len(new_ui_element) > 0, "New UI banner not found when feature flag is enabled."
    print("Feature flag enabled test passed.")
finally:
    driver.quit()