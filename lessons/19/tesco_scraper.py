from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import tesco_selectors as ts
import helpers as hp

class TescoScraper:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("Accept-Language=hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7")
        options.add_argument("Referer=https://bevasarlas.tesco.hu/")
        self.driver = webdriver.Chrome(options=options)
        url = "https://bevasarlas.tesco.hu/groceries/hu-HU/"
        self.driver.get(url)

    def scrape_tesco_main_categories(self):

        main_categories = self.driver.find_elements(by=By.XPATH, value=ts.get_tesco_main_categories_xpath())

        for main_category_id, main_category in enumerate(main_categories, 1):
            main_category_name = hp.get_row_from_multi_line_string(main_category.text, 1)
            print(main_category_name)
            main_category.click()
            time.sleep(2)
            self.scrape_tesco_mid_categories(main_category_name, main_category_id)
    
    def scrape_tesco_mid_categories(self, main_category_name, main_category_id):

        mid_categories = self.driver.find_elements(by=By.XPATH,
                                                   value=ts.get_tesco_mid_categories_xpath(main_category_id))
        
        for mid_category_id, mid_category in enumerate(mid_categories[2:], 3):
            mid_category_name = hp.get_row_from_multi_line_string(mid_category.text, 1)
            print(mid_category_name)
            mid_category.click()
            time.sleep(2)
        
            self.scrape_tesco_sub_categories(main_category_name, main_category_id, mid_category_name, mid_category_id)

    def scrape_tesco_sub_categories(self, main_category_name, main_category_id, mid_category_name, mid_category_id):

        sub_categories = self.driver.find_elements(by=By.XPATH, 
                                                   value=ts.get_tesco_sub_categories_xpath(main_category_id, mid_category_id))
        urls_to_scrape = []
        for sub_category in sub_categories[2:]:
            sub_category_name = hp.get_row_from_multi_line_string(sub_category.text, 1)
            print(sub_category_name)
            time.sleep(2)
            item = {
                "main_category": main_category_name,
                "mid_category": mid_category_name,
                "sub_category": sub_category_name,
                "sub_category_url": sub_category.find_element("tag name", "a").get_attribute("href")
            }
            urls_to_scrape.append(item)
        
        hp.save_data_to_csv(urls_to_scrape)
        
    def scrape_category_url_with_pagination(self, url: str):
        
        self.driver.get(url)
        time.sleep(5)

        num_of_pagination_buttons = len(self.driver.find_elements(by=By.CLASS_NAME,
                                                                  value=ts.get_tesco_subcategory_pagination_btn_class()))
        
        self.scrape_current_page(url, 2, 1)

        for page in range(3, num_of_pagination_buttons):
            next_page_button = self.driver.find_element(by=By.XPATH,
                                                        value=ts.get_tesco_subcategory_pagination_button_xpath(page))
            next_page_button.click()
            self.scrape_current_page(url, page, page -1)

    def scrape_current_page(self, url, div_index, page_index):

        print(f"Scraping url: {url} - page: {page_index}")

        time.sleep(5)

        products = self.driver.find_elements(by=By.XPATH, value=ts.get_tesco_product_list_xpath(div_index))
        product_list = []
        for product in products:
            product_dict = {}
            if "Ez a termék jelenleg nem elérhető" in product.text:
                continue

            product_dict["sub_category_url"] = url
            product_dict["product_name"] = hp.get_row_from_multi_line_string(product.text, 0)
            product_dict["price"] = re.sub(r" ", "", re.search(r"[\d ]+", 
                                        hp.get_row_from_multi_line_string(product.text,
                                        hp.find_single_ft_line(product.text))).group()) 
            print(product_dict["product_name"], product_dict["price"], "\n-----")
            product_list.append(product_dict)
            time.sleep(2)
        hp.save_data_to_csv(product_list, "lessons/19/tesco_product_data.csv")

tesco_scraper = TescoScraper()
#tesco_scraper.scrape_tesco_main_categories()

subcategory_list = hp.read_urls_from_csv("lessons/19/tesco_subcategory_urls.csv")
for item in subcategory_list:
    print(f"Scraping {item['sub_category']}...")
    tesco_scraper.scrape_category_url_with_pagination(item["sub_category_url"])
    print(f"Finished scraping {item['sub_category']}")

time.sleep(1000000)
tesco_scraper.driver.quit()
