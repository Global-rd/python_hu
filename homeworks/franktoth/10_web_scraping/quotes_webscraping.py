from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import csv
import time  # Import time for potential delays

class QuotesScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36") # Example user agent
        options.add_argument("--disable-blink-features=AutomationControlled")
        # You can add other options like "Accept-Language" or "Referer" if needed for this specific website.
        self.driver = webdriver.Chrome(options=options)
        self.url = "https://quotes.toscrape.com/"
        self.driver.get(self.url)

    def scrape_quotes(self):
        output_file = "quotes.csv"

        try:
            top_tags_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "tag-item"))
            )
            top_tags = [tag.find_element(By.TAG_NAME, "a").text.strip() for tag in top_tags_elements[:10]]
        except:  # Catching broad exceptions for simplicity in this example
            print("Error finding top tags.")
            self.driver.quit()
            return

        with open(output_file, "w", newline="", encoding="utf-8") as csvfile: #Added encoding
            writer = csv.writer(csvfile)
            writer.writerow(["Tag", "Author", "Quote"])

            for tag in top_tags:
                tag_url = urljoin(self.url, f"tag/{tag}")
                self.driver.get(tag_url)
                time.sleep(2)  # Add a short delay

                while True:
                    quotes = self.driver.find_elements(By.CLASS_NAME, "quote")
                    for quote in quotes:
                        try: #Added try except block, to handle cases where some elements are not found
                            author_element = quote.find_element(By.CLASS_NAME, "author")
                            quote_element = quote.find_element(By.CLASS_NAME, "text")
                            writer.writerow([tag, author_element.text.strip(), quote_element.text.strip()])
                        except:
                            print("Error finding author or quote element")

                    try:
                        next_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Next »")
                        if not next_button.is_enabled():
                            break
                        next_button.click()
                        time.sleep(2) #Added delay after click
                    except:
                        break

        print(f"Quotes scraped and saved to {output_file}")
        self.driver.quit()

if __name__ == "__main__":
    scraper = QuotesScraper()
    scraper.scrape_quotes()