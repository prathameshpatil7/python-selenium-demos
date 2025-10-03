from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

date_input = driver.find_element(By.ID, "datepicker")
date_input.click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[text()='15']").click()

selected_date = date_input.get_attribute("value")
print(f"Selected date: {selected_date}")
