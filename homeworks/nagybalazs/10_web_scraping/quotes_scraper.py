from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import quotes_selectors as qs
import helpers as hp


class QuotesScraper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=options)
        self.base_url = "https://quotes.toscrape.com/"
        self.driver.get(self.base_url)

    def get_top_tags(self):
        """
        Collects the top 10 tags from the main page.
        """
        tag_elements = self.driver.find_elements(By.CSS_SELECTOR, qs.get_top_tags_selector())
        tags = [tag.text for tag in tag_elements[:10]]
        return tags

    def scrape_quotes_by_tag(self, tag):
        """
        Scrapes all quotes for a given tag.
        """
        tag_url = f"{self.base_url}/tag/{tag}/"
        self.driver.get(tag_url)
        all_quotes = []

        while True:
            quote_elements = self.driver.find_elements(By.CSS_SELECTOR, qs.get_quotes_selector())
            for quote_el in quote_elements:
                quote_text = quote_el.find_element(By.CSS_SELECTOR, qs.get_quote_text_selector()).text.strip("“”")
                author = quote_el.find_element(By.CSS_SELECTOR, qs.get_quote_author_selector()).text
                all_quotes.append({"tag": tag, "author": author, "quote": quote_text})

            # Check for next page button
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, qs.get_next_button_selector())
                next_button.click()
                time.sleep(1)  # Wait for the next page to load
            except:
                break  # No more pages to navigate

        return all_quotes

    def scrape_top_tags(self):
        """
        Scrapes quotes for the top 10 tags and saves them to a CSV.
        """
        top_tags = self.get_top_tags()
        all_data = []

        for tag in top_tags:
            print(f"Scraping quotes for tag: {tag}")
            quotes = self.scrape_quotes_by_tag(tag)
            all_data.extend(quotes)

        hp.save_data_to_csv(all_data, "top_10_tags_quotes.csv")
        print("Scraping complete. Data saved to 'top_10_tags_quotes.csv'.")

    def close(self):
        self.driver.quit()
