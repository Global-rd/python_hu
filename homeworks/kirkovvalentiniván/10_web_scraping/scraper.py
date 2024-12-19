from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebScraper:
    def __init__(self, base_url, top_n=10):
        self.base_url = base_url
        self.top_n = top_n
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def get_top_tags(self):
        """Get the top N tags from the main page (right sidebar)."""
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-md-4 tags-box']//a")))
        
        # Find all the tags in the right sidebar
        tags = self.driver.find_elements(By.XPATH, "//div[@class='col-md-4 tags-box']//a")
        
        # Return top_n tags from the sidebar
        return [tag.text for tag in tags[:self.top_n]]
    
    def get_quotes_for_tag(self, tag):
        """Scrape all quotes for a specific tag, including pagination."""
        tag_url = f"{self.base_url}tag/{tag}/"
        quotes_data = []

        while True:
            self.driver.get(tag_url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='quote']")))

            quotes = self.driver.find_elements(By.XPATH, "//div[@class='quote']")
            for quote in quotes:
                text = quote.find_element(By.XPATH, ".//span[@class='text']").text
                author = quote.find_element(By.XPATH, ".//small[@class='author']").text
                quotes_data.append({"tag": tag, "author": author, "quote": text})

            try:
                next_button = self.driver.find_element(By.XPATH, "//li[@class='next']/a")
                tag_url = next_button.get_attribute("href")
            except Exception as e:
                print(f"Error: {e}. No more pages for tag '{tag}'")
                break  # No more pages

        return quotes_data
    
    def scrape_quotes(self):
        """Main function to scrape quotes by top N tags."""
        # Step 1: Get top tags
        top_tags = self.get_top_tags()
        print(f"Found top {self.top_n} tags: {top_tags}")

        # Step 2: Scrape quotes for each tag
        all_quotes = []
        for tag in top_tags:
            print(f"Scraping quotes for tag: {tag}")
            all_quotes.extend(self.get_quotes_for_tag(tag))

        return all_quotes

    def close(self):
        """Close the webdriver."""
        self.driver.quit()
