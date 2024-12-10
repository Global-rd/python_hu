from quotes_scraper import QuotesScraper

# Initialize the scraper
scraper = QuotesScraper()

# Scrape top 10 tags and save quotes
try:
    scraper.scrape_top_tags()
finally:
    scraper.close()
