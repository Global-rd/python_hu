# 3. PROGRAMTÖRZS, egy dedikált scraper class definiálásval: 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import toscrape_selectors as ts
import helpers as hp

class ToScrapeScraper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("Accept-Language=en-US,en;q=0.9")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://quotes.toscrape.com/")

    def scrape_top_tags(self):
        top_tags = self.driver.find_elements(by=By.XPATH, value=ts.get_top_tags_xpath())
        tag_urls = []

# Csak a top10 tag leszűrése:
        for tag in top_tags[:10]:  
            tag_name = tag.text
            tag_url = tag.get_attribute("href")
            tag_urls.append({'tag': tag_name, 'url': tag_url})
        
        return tag_urls

    def scrape_quotes_for_tag(self, tag_name, tag_url):
        self.driver.get(tag_url)
        time.sleep(2)

        quotes_data = []

# Végigloopolás az aktuális tag-hez tartozó valamennyi oldalon
        while True:
            quotes_elements = self.driver.find_elements(by=By.XPATH, value=ts.get_quote_elements_xpath())

            for quote_elem in quotes_elements:
                author = quote_elem.find_element(by=By.XPATH, value='.//*[@class="author"]').text
                quote = quote_elem.find_element(by=By.XPATH, value='.//*[@class="text"]').text

                quotes_data.append({
                    'tag': tag_name,
                    'author': author,
                    'quote': quote
                })
                time.sleep(1)

# Ellenőrzés: van-e következő oldal?
            next_page_button = self.driver.find_elements(by=By.XPATH, value=ts.get_next_page_button_xpath())
            if next_page_button:
                next_page_button[0].click()
                time.sleep(3)
            else:
                break

        hp.save_data_to_csv(quotes_data, "homeworks/veizerattila/10_web_scraping/quotes.csv")

    def scrape(self):
        tag_urls = self.scrape_top_tags()
        
        for tag_data in tag_urls:
            print(f"Idézetek scrape-elése, az alábbi tag-hez: {tag_data['tag']}")
            self.scrape_quotes_for_tag(tag_data['tag'], tag_data['url'])
            print(f"Idézetek scrape-elése lezárult a következő tag-hez: {tag_data['tag']}")

        self.driver.quit()

if __name__ == "__main__":
    scraper = ToScrapeScraper()
    scraper.scrape()
