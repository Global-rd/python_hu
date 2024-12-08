from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()
url = "https://quotes.toscrape.com/"
driver.get(url)

#top 10 tag
select_tags = [tag.text for tag in driver.find_elements(By.CSS_SELECTOR, '.tag-item a')[:10]] 

#eltárolandó adatok tárolása
data = []

for tag in select_tags:
    driver.get(url + "tag/" + tag + "/")
    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            data.append({
                "tag": tag, 
                "author": author, 
                "quote": text
            })

        try:
            next_button = driver.find_element(By.CLASS_NAME, "next")
            next_button.find_element(By.TAG_NAME, "a").click()
            WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

        except: 
            break    

driver.quit()

csv_file = "quotes_by_top_tags.csv"
with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "author", "quote"])
    writer.writeheader()
    writer.writerows(data)

