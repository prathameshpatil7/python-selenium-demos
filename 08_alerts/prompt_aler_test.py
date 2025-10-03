from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time  

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/alerts")
driver.maximize_window()

prompt_alert_button = driver.find_element(By.ID, "promptButton")
prompt_alert_button.click()
print("Prompt alert opened!")

prompt_alert = driver.switch_to.alert

print("Prompt alert message:", prompt_alert.text)

time.sleep(2) 

# Enter text in the prompt alert
prompt_alert.send_keys("Hello ! Prathamesh Here !!") # OR
# prompt_alert.dismiss()
print("Entered text in prompt alert.")

time.sleep(2)

prompt_alert.accept()
print("Prompt alert accepted!")
time.sleep(3)

second_alert = driver.switch_to.alert
print("second alert message you entered:", second_alert.text)

time.sleep(3)
second_alert.accept()

#close browser
driver.quit()