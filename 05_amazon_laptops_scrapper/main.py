
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()

# Base URL
base_url = "https://www.amazon.in/s?k=laptops&page={}"

laptop_data = []

# Loop through 10 pages
for page in range(1, 11):
    driver.get(base_url.format(page))
    time.sleep(3)

    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    for product in products:
        try:
            name = product.find_element(By.XPATH, ".//h2").text
        except:
            name = "N/A"
        try:
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text.replace(",", "")
        except:
            price = "N/A"
        try:
            rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text.split()[0]
        except:
            rating = "N/A"
        try:
            reviews = product.find_element(By.XPATH, ".//span[@class='a-size-base']").text.replace(",", "")
        except:
            reviews = "N/A"

        laptop_data.append([name, price, rating, reviews])

    time.sleep(2)

driver.quit()

# Save to CSV
with open("amazon_laptops_selenium.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product Name", "Price (INR)", "Rating", "Number of Reviews"])
    writer.writerows(laptop_data)

print("Scraping completed!!!")