import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "Accept-Language=hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7")
options.add_argument("Referer=https://quotes.toscrape.com/")
driver = webdriver.Chrome(options=options)


def scrape_top_tags(base_url):
    driver.get(base_url)
    top_tags = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
    return [tag.text for tag in top_tags[:10]]


def scrape_quotes_for_tag(base_url, tag):
    tag_url = f"{base_url}/tag/{tag}/"
    quotes = []
    while tag_url:
        driver.get(tag_url)
        time.sleep(1)  # Let the page load
        # Scrape quotes
        quote_elements = driver.find_elements(By.CSS_SELECTOR, ".quote")
        for quote_element in quote_elements:
            text = quote_element.find_element(By.CSS_SELECTOR, ".text").text
            author = quote_element.find_element(
                By.CSS_SELECTOR, ".author").text
            quotes.append({"tag": tag, "author": author, "quote": text})

        # Check if next page exists
        next_page = driver.find_elements(By.CSS_SELECTOR, ".next a")
        if next_page:
            tag_url = next_page[0].get_attribute("href")
        else:
            break
    return quotes


def save_to_csv(quotes, filename):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(quotes)


def main():
    base_url = "https://quotes.toscrape.com"
    try:
        top_tags = scrape_top_tags(base_url)
        all_quotes = []
        for tag in top_tags:
            all_quotes.extend(scrape_quotes_for_tag(base_url, tag))
        save_to_csv(all_quotes, "quotes_top_10_tags.csv")
        print("Scraping completed and saved to quotes_top_10_tags.csv.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
