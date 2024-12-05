import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install()) # ChromeDriver beállítása
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)  # maximum 10 másodpercig vár

try:
    # 1. Fő URL megnyitása
    driver.get("https://quotes.toscrape.com/")

    # 2. Top 10 tag
    tag_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tag-item > a")))
    tags = [tag.text for tag in tag_elements[:10]]  # Csak a top 10 tag
    print(f"A top 10 tag: {tags}")

    # Üres listát az idézetek tárolására
    quotes_data = []

    # Tageken végiglépked
    for tag in tags:
        print(f"A {tag} elemeinek beolvasasa.")
        driver.get(f"https://quotes.toscrape.com/tag/{tag}/")

        # Pagination!
        while True:
            # Aktuális oldal
            quote_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.quote')))
            for quote in quote_elements:
                text = quote.find_element(By.CSS_SELECTOR, '.text').text
                author = quote.find_element(By.CSS_SELECTOR, '.author').text
                quotes_data.append([tag, author, text])

            # Van-e következő oldal?
            next_button = driver.find_elements(By.CSS_SELECTOR, '.next > a')
            if next_button:
                next_button[0].click() 
                wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.quote')))
            else:
                break

    # Mentés CSV fájlba
    df = pd.DataFrame(quotes_data, columns=['tag', 'author', 'quote'])
    print("Mentes a quotes.csv fajlba")
    df.to_csv('quotes.csv', index=False, encoding='utf-8')

finally:
    driver.quit()