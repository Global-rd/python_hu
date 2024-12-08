# 1. HELPER function-ök definiálása, külön .py állományban:

import pandas as pd

csv_path = "homeworks/veizerattila/10_web_scraping/quotes.csv"
pd.set_option("display.max_colwidth", 100)

# scrapelt adatok beolvasása .csv-be
def save_data_to_csv(data, filename=csv_path):
    df = pd.DataFrame(data)
    if data:
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
    print(f"Adatok sikeresen lementve az alábbi állományba: {filename}")


#.csv beolvasása Pandas dataframe-be
def read_csv_to_dataframe(filename=csv_path):
    
    df = pd.read_csv(filename)
    return df