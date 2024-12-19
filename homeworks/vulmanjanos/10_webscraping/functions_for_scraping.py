from selenium import webdriver
from selenium.webdriver.common.by import By

def initialize_driver():
    # Initialize the WebDriver for Edge
    driver = webdriver.Edge()
    return driver

def get_top_tags(driver):
    # Open the URL
    driver.get("https://quotes.toscrape.com/")
    
    # Get the top 10 tags
    top_tags = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")[:10]
    top_tags = [tag.text for tag in top_tags]
    return top_tags

def scrape_quotes_for_tag(driver, tag):
    quotes_data = []
    page = 1
    while True:
        # Construct the URL for the tag and page
        url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
        driver.get(url)
        
        # Get the quotes on the current page
        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
        
        # If no quotes are found, break the loop (end of pagination)
        if not quotes:
            break
        
        # Extract data from each quote
        for quote in quotes:
            text = quote.find_element(By.CSS_SELECTOR, ".text").text
            author = quote.find_element(By.CSS_SELECTOR, ".author").text
            quotes_data.append([tag, author, text])
        
        # Go to the next page
        page += 1
    
    return quotes_data