import pandas as pd

def quotes_split(text:str):
    return text.split("\n")

def get_author_by(text:str):
    return text.split("by")[1]

def get_author_about(text:str):
    return text.split("(about)")[0]

def get_author(text:str):
    return text.strip()

def save_data_to_csv(data, filename="homeworks/nagynorbert/quotes.csv"):
    
    df = pd.DataFrame(data)
    if data:
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
        print(f"Data written to {filename}")