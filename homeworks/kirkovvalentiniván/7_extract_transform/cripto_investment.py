import requests
import pandas as pd

class CoingeckoAPI: 
    
    def __init__(self, base_url, params):
        self.base_url = base_url
        self.params = params 
    
        self.raw_data = None

    def get_data(self):
        response = requests.get(self.base_url, params = self.params)
        if response.status_code == 200:
            print("Data is extracted successfully.")
            return response.json()
        else:
            raise Exception(f" API error: {response.status_code}, {response.text}")

class ResponseTransformation:    

    def __init__(self, raw_data):
        
        if not raw_data:
            raise ValueError("There is no raw data or something went wrong.")
        self.df = pd.DataFrame(raw_data)
        print("Dataframe is created successfully.")
        
    def count_missing_values(self):
        """Count missing values in the DataFrame."""
        return self.df.isnull().sum()

    def calculate_total_market_cap(self):
        """Calculate the total market capitalization."""
        return self.df["market_cap"].sum()
        
    def get_top_n(self, column_name, n):
        """Get the top n cryptocurrencies based on the choosen column."""
        return self.df.nlargest(n, column_name)
    
    def sort_by_column(self, column_name, ascending=True):
        """Sort data by column name."""
        return self.df.sort_values(column_name,ascending=ascending)
    
    def add_change_direction_column(self, source_column, new_column):

        def classify_change(change):
            if change > 0:
                return "+"
            elif change < 0:
                return "-"
            else:
                return 0
        self.df[new_column] = self.df[source_column].apply(classify_change)
        print(f"{new_column} column is added successfully.")
        

# Run the process
if __name__ == "__main__":

    base_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1
    }
    
    #Set up connection to the API
    api = CoingeckoAPI(base_url, params)

    #Extract the data
    raw_data = api.get_data()

    #Create the dataframe using the function
    transformer = ResponseTransformation(raw_data)

    #Counting empty cells
    missing_values = transformer.count_missing_values()
    print("Empty values per columns: ")
    print(missing_values)

    #Calculating total market cap
    total_market_cap = transformer.calculate_total_market_cap()
    print(f"Total market cap is: {total_market_cap}.")

    #Top 50 crypto currency group by the "current_price" column
    top50df = transformer.get_top_n("current_price", 50)
    print(f"Top 50 crypto currencies based on the 'current_price' are: ")
    print(top50df)

    #Sort based on the price change
    sorted_top50_df = transformer.sort_by_column("price_change_percentage_24h", ascending=False)
    print("Top 50 crypto currency based on the price change percentage: ")
    print(sorted_top50_df)

    # 7. Add new column for representing the change of the diredtion of the prices
    transformer.add_change_direction_column("price_change_percentage_24h", "change_direction")
    print("The DataFrame updated with the direction changed column: ")
    print(transformer.df.head())
