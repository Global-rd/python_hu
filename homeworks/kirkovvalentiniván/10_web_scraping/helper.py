import csv
import pandas as pd

def save_to_csv(data, filename="/homeworks/kirkovvalentiniván/10_web_scraping/quotes.csv"):
    """Save a list of dictionaries to a CSV file."""
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, mode="a", index=False, header=not pd.io.common.file_exists(filename))

def read_from_csv(filename="/homeworks/kirkovvalentiniván/10_web_scraping/quotes.csv"):
    """Read data from a CSV file into a DataFrame."""
    try:
        df = pd.read_csv(filename, encoding="utf-8")
        return df
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return pd.DataFrame()  # Returning an empty DataFrame on failure
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return pd.DataFrame()
