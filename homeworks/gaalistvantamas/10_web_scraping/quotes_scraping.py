"""
Author: Gaál István Tamás
Task: Homework-10
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time
import quotes_selectors as qs

MAX_TAGS = 10
MAX_QUOTES_PER_PAGE = 15

class QuotesScraper:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("Accept-Language=hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7")
        options.add_argument("https://quotes.toscrape.com/")
        self.driver = webdriver.Chrome(options=options)
        url = "https://quotes.toscrape.com/"
        self.driver.get(url)

    def scrape_top_ten_categories(self):
        top_ten_category =[]
        
        for i in range(1,MAX_TAGS+1):
            top_ten_categories = self.driver.find_element(by=By.XPATH, value= qs.get_quotes_top_ten_category_xpath(i)) 
            top_ten_category.append(top_ten_categories.text)
        
        return top_ten_category

    def get_author_and_text(self, category, index):
        
        author = self.driver.find_element(by=By.XPATH, value= qs.get_author_from_the_chosen_tag_xpath(index))
        quotes_text = self.driver.find_element(by=By.XPATH, value= qs.get_quote_text_from_the_chosen_tag_xpath(index))
            
        item = {
            "tag_name": str(category),
            "author": str(author.text),
            "text": str(quotes_text.text)
            }
        
        return item
    
    def save_datas_to_csv(self, data, filename="homeworks/gaalistvantamas/10_web_scraping/quotes_top_ten_tags.csv"):

        df = pd.DataFrame(data)
        
        if data:
            df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
            print(f"Data written to {filename}")
        

    def scrape_quotes_data_from_tags(self, top_ten_category):
        
        datas = []
        
        for category in top_ten_category:
            self.driver.get(f"https://quotes.toscrape.com/tag/{category}")
            index = 0
            OK = True
        
            for i in range(1,MAX_QUOTES_PER_PAGE):
                try: 
                    if (self.driver.find_element(by=By.XPATH, value= qs.get_quotes_from_the_tag(i))):
                        datas.append(self.get_author_and_text(category, i))
                        index += 1    
                except:
                    OK = False
                    pass

            if OK == False:
                try:
                    self.driver.find_element(by=By.XPATH, value=qs.get_pagination_button_xpath()).click()
                    for i in range(1,MAX_QUOTES_PER_PAGE):
                        try: 
                            if (self.driver.find_element(by=By.XPATH, value= qs.get_quotes_from_the_tag(i))):
                                datas.append(self.get_author_and_text(category, i))
                                index += 1
                        except:        
                            pass
                except:
                    pass
           
            print(f"{category} : {index}")
        self.save_datas_to_csv(datas)

quotes_scraper = QuotesScraper()

quotes_scraper.scrape_quotes_data_from_tags(quotes_scraper.scrape_top_ten_categories())

time.sleep(1000000)
quotes_scraper.driver.quit()
