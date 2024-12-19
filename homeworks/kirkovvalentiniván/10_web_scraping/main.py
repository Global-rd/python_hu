from scraper import WebScraper
from helper import save_to_csv
from config import BASE_URL, OUTPUT_FILE

def main():
    """Main function to scrape quotes by top 10 tags."""
    # Initialize the scraper class
    scraper = WebScraper(BASE_URL)
    
    try:
        # Step 1: Scrape quotes by top tags
        all_quotes = scraper.scrape_quotes()

        # Step 2: Save the data to a CSV file
        save_to_csv(all_quotes, OUTPUT_FILE)
        print(f"Scraped data saved to {OUTPUT_FILE}")

    finally:
        scraper.close()

if __name__ == "__main__":
    main()
