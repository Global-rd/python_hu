from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import os

# ChromeDriver path
CHROMEDRIVER_PATH = '/path/to/chromedriver'  # Add the correct path to your chromedriver

# Initialize WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Base URL
BASE_URL = "https://quotes.toscrape.com"

# Get top 10 tags
def get_top_tags(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tag-item")))
    tags = driver.find_elements(By.CLASS_NAME, "tag-item")[:10]
    top_tags = [tag.text for tag in tags]
    return top_tags

# Scrape quotes for a specific tag
def scrape_quotes_for_tag(driver, tag):
    quotes_data = []
    url = f"{BASE_URL}/tag/{tag}/"
    while True:
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
        except TimeoutException:
            break

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote_element in quotes:
            quote_text = quote_element.find_element(By.CLASS_NAME, "text").text
            author = quote_element.find_element(By.CLASS_NAME, "author").text
            quotes_data.append({"tag": tag, "author": author, "quote": quote_text})

        # Check if next page exists
        try:
            next_button = driver.find_element(By.CLASS_NAME, "next")
            url = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            break

    return quotes_data

# Save data to CSV
def save_to_csv(data, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(data)

# Main function
def main():
    try:
        top_tags = get_top_tags(driver)
        all_quotes = []

        for tag in top_tags:
            quotes = scrape_quotes_for_tag(driver, tag)
            all_quotes.extend(quotes)

        # Create output directory
        output_dir = os.path.join(os.getcwd(), "10_web_scraping")
        os.makedirs(output_dir, exist_ok=True)

        # Save to CSV
        output_file = os.path.join(output_dir, "quotes.csv")
        save_to_csv(all_quotes, output_file)

        print(f"Data successfully saved to {output_file}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
