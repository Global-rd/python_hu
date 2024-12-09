from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd

class WebScraper:
    def __init__(self, url, driver_path=None):
        self.url = url
        if driver_path:
            self.driver = webdriver.Chrome(executable_path=driver_path)
        else:
            self.driver = webdriver.Chrome()
        self.data = []

    # ---------------------- TOP 10 Cimke listába gyűjtése ----------------------
    def scrape_tags(self):
        self.driver.get(self.url)
        top_ten_tag_list = [tag.text for tag in self.driver.find_elements(By.CSS_SELECTOR, '.tag-item a')[:10]]
        return top_ten_tag_list

    # --------------------- Idézet szövegek összegyűjtése ---------------------
    def scrape_quotes(self, tag):
        self.driver.get(self.url + "tag/" + tag + "/")
        while True: 
            quotes = self.driver.find_elements(By.CLASS_NAME, "quote")
            for quote in quotes: 
                quote_text = quote.find_element(By.CLASS_NAME, "text").text
                author = quote.find_element(By.CLASS_NAME, "author").text
                self.data.append({
                    "tag": tag,
                    "author": author,
                    "quote": quote_text
                })

            try: # ---------------------- next button keresése ----------------------
                next_page_button = self.driver.find_element(By.CLASS_NAME, "next")
                next_page_button.find_element(By.TAG_NAME, "a").click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))
            except:
                break

# -------------------------------- Adatok fájlba írása --------------------------------
    def save_data_to_csv(self, filename="quotes_data_v04.csv"):
        df = pd.DataFrame(self.data)
        if self.data:
            df.to_csv(filename, mode='a', index=False, header=not os.path.exists(filename))
            print(f"Data scraped to {filename}")

# -------------------------------- Folyamat működtetése:  --------------------------------
# --------------- Cimkék és idézetek összegyűjtése, böngésző bezárása, adatok mentése ---------------
    def run(self):
        tags = self.scrape_tags()
        for tag in tags:
            self.scrape_quotes(tag)
        self.driver.quit()
        self.save_data_to_csv("python_hu/homeworks/valitothattila/10_web_scraping/quotes_data_v05.csv")



# --------------------------------- Main függvény ---------------------------------
if __name__ == "__main__":
    url = "https://quotes.toscrape.com/"
    scraper = WebScraper(url)
    scraper.run()
