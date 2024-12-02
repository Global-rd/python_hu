import pandas as pd

def get_row_from_multi_line_string(multiline_string: str, index:int) -> str:
    return multiline_string.split("\n")[index]


def find_single_ft_line(multiline_string):
    lines = multiline_string.splitlines()
    
    for index, line in enumerate(lines):
        if line.count("Ft") == 1:
            return index 
        
    return None

def save_data_to_csv(data, filename="lessons/19/tesco_subcategory_urls.csv"):
    
    df = pd.DataFrame(data)
    if data:
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
        print(f"Data written to {filename}")

def read_urls_from_csv(path:str):
    
    df = pd.read_csv(path)
    return df.to_dict(orient='records')




