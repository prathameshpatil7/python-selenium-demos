from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/alerts")

#find alert button
alert_button = driver.find_element(By.ID, "alertButton")

#click on alert button
alert_button.click()

#switch focus to alert pop-up
alert = driver.switch_to.alert

#print alert message
print("Simple alert message:", alert.text)

time.sleep(5)
alert.accept()

driver.quit()