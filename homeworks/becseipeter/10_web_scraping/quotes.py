import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# URL of the website
BASE_URL = "https://quotes.toscrape.com"

# Initialize WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Get the top 10 tags
def get_top_tags(driver):
    driver.get(BASE_URL)
    tag_elements = driver.find_elements(By.CSS_SELECTOR, 'div.tags-box a.tag')
    top_tags = [tag.text for tag in tag_elements[:10]]
    return top_tags

# Scrape quotes for a specific tag
def scrape_quotes_for_tag(driver, tag):
    quotes = []
    page = 1
    while True:
        driver.get(f"{BASE_URL}/tag/{tag}/page/{page}/")
        try:
            quote_elements = driver.find_elements(By.CSS_SELECTOR, 'div.quote')
            for quote_element in quote_elements:
                text = quote_element.find_element(By.CSS_SELECTOR, 'span.text').text
                author = quote_element.find_element(By.CSS_SELECTOR, 'span small.author').text
                quotes.append({
                    'tag': tag,
                    'author': author,
                    'quote': text
                })
            # Check if there's a next page
            next_button = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
            if next_button:
                page += 1
            else:
                break
        except NoSuchElementException:
            break
    return quotes

# Write data to a CSV file
def write_to_csv(data, filename="top10_quotes.csv"):
    # Ensure the directory exists
    output_dir = "10_web_scraping"
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    filepath = os.path.join(output_dir, filename)

    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['tag', 'author', 'quote'])
        writer.writeheader()
        writer.writerows(data)

    print(f"File saved at: {filepath}")

# Main script
def main():
    driver = init_driver()
    try:
        print("Collecting top tags...")
        top_tags = get_top_tags(driver)

        all_quotes = []
        for tag in top_tags:
            print(f"Scraping quotes for tag: {tag}")
            quotes = scrape_quotes_for_tag(driver, tag)
            all_quotes.extend(quotes)

        print(f"Writing {len(all_quotes)} quotes to CSV...")
        write_to_csv(all_quotes, filename="top10_quotes.csv")

        print("Scraping completed successfully!")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
