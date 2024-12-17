import csv
from functions_for_scraping import initialize_driver, get_top_tags, scrape_quotes_for_tag

# Initialize the WebDriver for Edge
driver = initialize_driver()

# Get the top 10 tags from the website
top_tags = get_top_tags(driver)

all_quotes_data = []
# Scrape quotes for each of the top 10 tags
for tag in top_tags:
    quotes_data = scrape_quotes_for_tag(driver, tag)
    all_quotes_data.extend(quotes_data)

# Close the WebDriver
driver.quit()

# Open a new CSV file to write the results

with open(r"/Users/janos/PYTHON/python_rd_repo_python_hu/python_hu/homeworks/vulmanjanos/10_webscraping/quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write the header row to the CSV file
    writer.writerow(["tag", "author", "quote"])
    
    # Iterate over all quotes data and write each quote to the CSV file
    for quote_data in all_quotes_data:
        writer.writerow(quote_data)

print("Scraping completed and data saved to quotes.csv.")