from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Doe")
driver.find_element(By.ID, "sex-0").click()
driver.find_element(By.ID, "exp-2").click()
driver.find_element(By.ID, "datepicker").send_keys("03/10/2025")

profession_checkbox = driver.find_element(By.ID, "profession-1")
driver.execute_script("arguments[0].scrollIntoView(true);", profession_checkbox)
driver.execute_script("arguments[0].click();", profession_checkbox)

driver.find_element(By.ID, "tool-2").click()
Select(driver.find_element(By.ID, "continents")).select_by_visible_text("Asia")
commands = Select(driver.find_element(By.ID, "selenium_commands"))
commands.select_by_visible_text("Browser Commands")
commands.select_by_visible_text("Navigation Commands")
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("Form submitted successfully.")
driver.quit()