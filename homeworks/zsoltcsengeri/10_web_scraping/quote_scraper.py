from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import save_data_to_csv
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the main URL
driver.get("https://quotes.toscrape.com/")

# JavaScript-based extraction for the top 10 tags
print("Extracting Top 10 Tags using JavaScript...")
top_tags = driver.execute_script("""
    return Array.from(document.querySelectorAll('.tags-box .tag-item a')).map(tag => tag.textContent.trim());
""")
if top_tags:
    print(f"Top 10 Tags: {top_tags}")
else:
    print("No tags found! Exiting script.")
    driver.quit()
    exit()

# Prepare a list to store the scraped data
scraped_data = []

# Loop through each tag and scrape quotes
for current_tag in top_tags:
    print(f"Scraping quotes for tag: {current_tag}")

    # Construct the URL for the current tag
    tag_url = f"https://quotes.toscrape.com/tag/{current_tag}/"
    driver.get(tag_url)

    # Handle pagination for the current tag
    while True:
        # Wait for the quotes to load on the page
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
            )
        except Exception as e:
            print(f"Error while waiting for quotes: {str(e)}")
            break

        # Extract all quote blocks on the current page
        quote_blocks = driver.find_elements(By.XPATH, "//div[@class='quote']")

        # Extract data from each quote block
        for block in quote_blocks:
            # Extract quote text
            quote_text = block.find_element(By.XPATH, ".//span[@class='text']").text

            # Extract author name
            author_name = block.find_element(By.XPATH, ".//small[@class='author']").text

            # Append the data to the scraped_data list
            scraped_data.append({
                "tag": current_tag,
                "author": author_name,
                "quote": quote_text,
            })

        # Check if there's a "Next" button for pagination
        try:
            next_button = driver.find_element(By.XPATH, "//li[@class='next']/a")
            next_button.click()  # Go to the next page
            time.sleep(2)  # Delay to prevent rapid requests
        except Exception:
            print(f"No more pages for tag: {current_tag}")
            break  # Exit the loop if there's no "Next" button

# Save the scraped data to a CSV file
if scraped_data:
    save_data_to_csv(scraped_data, "top_10_tags_quotes.csv")
    print("Data saved successfully!")
else:
    print("No data scraped.")

# Close the browser
driver.quit()
