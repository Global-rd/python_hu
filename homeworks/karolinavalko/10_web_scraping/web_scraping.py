from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import pandas as pd
import quote_selector as qs
import helpers as hp

class QuoteScraper:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("Accept-Language=hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7")
        options.add_argument("Referer=https://quotes.toscrape.com/")
        self.driver = webdriver.Chrome(options=options)
        url = "https://quotes.toscrape.com/"
        self.driver.get(url)

    def get_top_tags(self, max_tags):

        top_tags = self.driver.find_elements(by=By.XPATH, value=qs.get_tags_xpath())
        tag_urls = []

        for tag in top_tags[:max_tags]:  
            tag_name = tag.text
            tag_url = tag.get_attribute("href")
            tag_urls.append({'tag': tag_name, 'url': tag_url})

        return tag_urls

    def get_quotes(self, tag):
        self.driver.get(tag['url'])
        time.sleep(2)

        authors = []
        quotes = []
        tags = []

        while True:
            quotes_elements = self.driver.find_elements(by=By.XPATH, value=qs.get_quote_elements_xpath())

            for quote_elem in quotes_elements:
                authors.append(quote_elem.find_element(by=By.XPATH, value='.//*[@class="author"]').text)
                quotes.append(quote_elem.find_element(by=By.XPATH, value='.//*[@class="text"]').text)
                tags.append(tag['tag'])

            next_page_button = self.driver.find_elements(by=By.XPATH, value=qs.get_next_page_button_xpath())
            if next_page_button:
                next_page_button[0].click()
                time.sleep(3)
            else:
                break
            
            return pd.DataFrame({
                    'tag': tags,
                    'author': authors,
                    'quote': quotes
                })
    


quote_scraper= QuoteScraper()
top_tags = quote_scraper.get_top_tags(10)
all_quotes = pd.DataFrame()
for tag in top_tags:
    print(f'now reading tag {tag['tag']}...')
    all_quotes = pd.concat([all_quotes,quote_scraper.get_quotes(tag)])
all_quotes.to_csv('homeworks/karolinavalko/10_web_scraping/quotes_with_top_ten_tags.csv',index=False)
quote_scraper.driver.quit()