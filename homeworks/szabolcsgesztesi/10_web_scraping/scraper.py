from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

# Selenium driver beállítása Chrome-hoz
driver = webdriver.Chrome()
url = "https://quotes.toscrape.com/"
driver.get(url)

# A top 10 tag kigyűjtése
top_tags = []
tag_elements = driver.find_elements(By.CSS_SELECTOR, '.tag-item a')[:10]
for tag in tag_elements:
    top_tags.append(tag.text)

# Az idézetek kigyűjtése
data = []

for tag in top_tags:
    driver.get(f"{url}tag/{tag}")
    while True:
        quotes = driver.find_elements(By.CSS_SELECTOR, '.quote')
        for quote in quotes:
            text = quote.find_element(By.CSS_SELECTOR, '.text').text
            author = quote.find_element(By.CSS_SELECTOR, '.author').text
            data.append({
                "tag": tag,
                "author": author,
                "quote": text
            })
        # Lapozás kezelése
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.pager .next a')
            next_button.click()
            time.sleep(1)  # Biztosítsd, hogy az oldal teljesen betöltődjön
        except:
            break

# Eredmények mentése CSV-be
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['tag', 'author', 'quote']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

driver.quit()