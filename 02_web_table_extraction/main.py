from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    driver.maximize_window()

    table = driver.find_element(By.ID, "customers")

    # Extracting all rows from the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Iterating through each row and extract columns
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
        col_texts = [col.text.upper() for col in cols]
        print(col_texts)
        print(" | ".join(col_texts))

finally:
    driver.quit()
