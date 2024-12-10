from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import save_data_to_csv

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://quotes.toscrape.com/")

# Extract quotes, authors, and tags for each quote block
quote_blocks = driver.find_elements(By.XPATH, "//div[@class='quote']")

# Prepare an empty list for scraped data
scraped_data = []

# Loop through each quote block
for block in quote_blocks:
    # Extract quote text
    quote_text = block.find_element(By.XPATH, ".//span[@class='text']").text
    
    # Extract author name
    author_name = block.find_element(By.XPATH, ".//small[@class='author']").text
    
    # Extract tags associated with this quote
    quote_tags = [tag.text for tag in block.find_elements(By.XPATH, ".//div[@class='tags']/a")]
    
    # Combine the data
    scraped_data.append({
        "quote": quote_text,
        "author": author_name,
        "tag": ", ".join(quote_tags)  # Join multiple tags with a comma
    })

# Save the data to a CSV file
save_data_to_csv(scraped_data, "quotes.csv")

# Close the browser
driver.quit()
