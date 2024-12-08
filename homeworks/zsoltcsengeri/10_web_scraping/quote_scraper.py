from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import save_data_to_csv

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://quotes.toscrape.com/")

# Extract quotes and authors
quotes = driver.find_elements(By.XPATH, "//div[@class='quote']/span[@class='text']")
authors = driver.find_elements(By.XPATH, "//div[@class='quote']/span/small[@class='author']")

# Prepare lists for storing data
quote_texts = []
author_names = []

# Extract quotes
for quote in quotes:
    quote_texts.append(quote.text)

# Extract authors
for author in authors:
    author_names.append(author.text)

# Combine data into a list of dictionaries
scraped_data = []
for i in range(len(quote_texts)):
    scraped_data.append({
        "tag": "example_tag",  # Replace with actual tag
        "author": author_names[i],
        "quote": quote_texts[i]
    })

# Save the data to a CSV file
save_data_to_csv(scraped_data, "quotes.csv")

# Close the browser
driver.quit()
