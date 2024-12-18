import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Setup the webdriver
driver = webdriver.Chrome()

# Function to get the top 10 tags
def get_top_tags():
    driver.get("https://quotes.toscrape.com/")
    tags = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
    top_tags = [tag.text for tag in tags[:10]]
    return top_tags

# Function to scrape quotes for a given tag
def scrape_quotes_for_tag(tag):
    quotes = []
    page = 1
    while True:
        url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
        driver.get(url)
        time.sleep(2)  # Adding delay to allow page to load
        
        quote_elements = driver.find_elements(By.CSS_SELECTOR, ".quote")
        if not quote_elements:
            break  # No more quotes, exit the loop
        
        for quote_element in quote_elements:
            text = quote_element.find_element(By.CSS_SELECTOR, ".text").text
            author = quote_element.find_element(By.CSS_SELECTOR, ".author").text
            quotes.append({"tag": tag, "author": author, "quote": text})
        
        page += 1

    return quotes

# Main function to scrape all quotes for top 10 tags and save to a CSV
def scrape_quotes():
    top_tags = get_top_tags()
    all_quotes = []
    
    for tag in top_tags:
        quotes = scrape_quotes_for_tag(tag)
        all_quotes.extend(quotes)
    
    # Save to CSV
    df = pd.DataFrame(all_quotes)
    output_path = "homeworks/taridaniel/10_web_scraping/quotes.csv"
    print(f"Saving data to {output_path}")
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
    
    driver.quit()

# Run the scraper
scrape_quotes()
