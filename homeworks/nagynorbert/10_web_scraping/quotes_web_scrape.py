from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import re
#import time
import quotes_selectors as qs
import quotes_helper as hp

class QuotesScraper:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("Accept-Language=hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7")
        options.add_argument("Referer=https://quotes.toscrape.com/")
        self.driver = webdriver.Chrome(options=options)
        self.url = "https://quotes.toscrape.com/"
        self.driver.get(self.url)
        self.scrape_object_list = []

    def scrape_object_list_append(self,tag,page_size):
        self.scrape_object_list.append({"tag": tag, "page_size": page_size})
    
    def get_scrape_object_list(self):
        return self.scrape_object_list
    
    def get_top_10_tags(self):
        
        top_10_tags = self.driver.find_elements(by=By.XPATH,value=qs.get_top_10_tags_xpath())
        
        top_10_tag_list = []
        for tag in top_10_tags:
            top_10_tag_list.append(tag.text)
        return top_10_tag_list
    
    def get_page_for_tags(self,tag_list):

        for tag in tag_list:
            page_num = 1
            while True:
                new_url = self.url + "tag" + f"/{tag}/page/{page_num}"
                self.driver.get(new_url)
                #using find_element to avoid NoSuchElemntExecption
                next_page = self.driver.find_elements(by=By.XPATH,value=qs.next_page_xpath())
                if len(next_page) == 1:
                    page_num += 1
                else:
                    self.scrape_object_list_append(tag=tag,page_size=page_num)
                    break
        return True
    
    def get_tag_author_quote_per_page(self,scraped_list):

        collected_data = []
        for item in scraped_list:
            tag = item.get("tag")
            for page_num in range(1,item.get("page_size")):
                 new_url = self.url + "tag" + f"/{tag}/page/{page_num}"
                 self.driver.get(new_url)
                 quotes = self.driver.find_elements(by=By.XPATH,value=qs.quote_xpath())
                 for q in quotes:
                    quote_text = hp.quotes_split(q.text)[0].strip()
                    author_text = hp.quotes_split(q.text)[1].strip()
                    author = hp.get_author((hp.get_author_about((hp.get_author_by(author_text)))))
                    quote_item = {
                        "quote": quote_text,
                        "author": author,
                        "tag": tag
                    }
                    collected_data.append(quote_item)                     
        return collected_data
                     

quotes_scarper = QuotesScraper()
quotes_scarper.get_page_for_tags(quotes_scarper.get_top_10_tags())
hp.save_data_to_csv(quotes_scarper.get_tag_author_quote_per_page(quotes_scarper.get_scrape_object_list()))
quotes_scarper.driver.quit()