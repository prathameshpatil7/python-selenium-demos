from selenium import webdriver  
from selenium.webdriver.common.by import By 
import time  

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/alerts")

confirm_alert_button = driver.find_element(By.ID, "confirmButton")

confirm_alert_button.click()

confirm_alert = driver.switch_to.alert

print("Confirm alert message:", confirm_alert.text)

time.sleep(5)
#confirm_alert.accept() #accept to click on ok
confirm_alert.dismiss() #to cancel alert
time.sleep(3)

simple_alert = driver.switch_to.alert
time.sleep(3)
simple_alert.accept()


driver.quit()