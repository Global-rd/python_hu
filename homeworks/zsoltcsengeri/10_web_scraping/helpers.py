import pandas as pd

def save_data_to_csv(data, filename="scraped_data.csv"):
    """
    Saves a list of dictionaries to a CSV file.
    
    :param data: List of dictionaries, where each dictionary is a row in the CSV.
    :param filename: Name of the output CSV file (default: scraped_data.csv).
    """
    if data:  # Check if there's any data to save
        df = pd.DataFrame(data)  # Convert list of dicts to a DataFrame
        if not df.empty:  # Check if DataFrame is not empty
            df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
            print(f"Data successfully saved to {filename}")
        else:
            print("No data to save!")
    else:
        print("Data list is empty. Nothing to save.")
