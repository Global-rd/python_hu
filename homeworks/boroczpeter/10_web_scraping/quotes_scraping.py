from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# selenium WebDriver in chrome browser
driver = webdriver.Chrome()

# determine base URL
BASE_URL = "https://quotes.toscrape.com/"

# navigate to the website and collect the top 10 tags
try:
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    
    # locate top 10 tags and get them for choosing
    tags_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tags-box")))
    tags = [tag.text for tag in tags_element.find_elements(By.TAG_NAME, "a")[:10]]
    
    # data storage
    all_quotes = []

# browsing the tags and collect the relevant quotes
    for tag in tags:
        tag_url = f"{BASE_URL}tag/{tag}/"
        while True:
            driver.get(tag_url)
            
            # wait for the quotes to load
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
            
            # etract quotes, authors, and original tag
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            for quote_element in quotes:
                quote_text = quote_element.find_element(By.CLASS_NAME, "text").text
                author = quote_element.find_element(By.CLASS_NAME, "author").text
                all_quotes.append({"tag": tag, "author": author, "quote": quote_text})
            
            # pagination, check for the "Next" button
            try:
                next_button = driver.find_element(By.CLASS_NAME, "next")
                next_page = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
                tag_url = next_page  # update URL for the next page
            except:
                break

finally:
    # close the WebDriver
    driver.quit()

# save the quotes to a CSV file
quotes_df = pd.DataFrame(all_quotes)
quotes_df.to_csv("top_10_quotes.csv", index=False)

print("Scraping completed. Data saved to 'top_10_quotes.csv'.")