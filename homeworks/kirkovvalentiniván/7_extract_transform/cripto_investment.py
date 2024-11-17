import requests
import pandas as pd

class CoingeckoAPI: 
    
    def __init__(self,vs_currency = "usd", order = "market_cap_desc", per_page = 250, page = 1):
        self.base_url = "https://api.coingecko.com/api/v3/coins/markets"
        self.params = {
        "vs_currency": vs_currency,
        "order": order,
        "per_page": per_page,
        "page": page
        }
    
        self.raw_data = None
        self.df = None

    def get_data(self):
        response = requests.get(self.base_url, params = self.params)
        if response.status_code == 200:
            self.raw_data = response.json()
            print("Data is extracted successfully.")
        else:
            raise Exception(f" API error: {response.status_code}, {response.text}")

    def create_dataframe(self):
        """Convert the get_data into a Pandas DataFrame."""
        if self.raw_data is None:
            raise ValueError("There is no data after the pull. First run the get_data method!")
        self.df = pd.DataFrame(self.raw_data)
        print("DataFrame is created successfully.")
        
    def count_missing_values(self):
        """Count missing values in the DataFrame."""
        if self.df is None:
            raise ValueError("DataFrame is not created. First run the create_dataframe() method!")
        return self.df.isnull().sum()

    def calculate_total_market_cap(self):
        """Calculate the total market capitalization."""
        if self.df is None:
            raise ValueError("DataFrame is not created. First run the create_dataframe() method!")
        return self.df["market_cap"].sum()
        
    def get_top_n(self, column_name, n):
        """Get the top n cryptocurrencies based on the choosen column."""
        if self.df is None:
            raise ValueError("DataFrame is not created. First run the create_dataframe() method!")
        return self.df.nlargest(n, column_name)
    
    def sort_by_column(self, column_name, ascending=True):
        """Sort data by column name."""
        if self.df is None:
            raise ValueError("DataFrame is not created. First run the create_dataframe() method!")
        return self.df.sort_values(column_name,ascending=ascending)
    
    def add_change_direction_column(self, source_column, new_column):
        if self.df is None:
            raise ValueError("Dataframe is not created. First run the create_dataframe() method!")
        else:

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

    #Set up connection to the API
    api = CoingeckoAPI(vs_currency="usd", order="market_cap_desc", per_page=250, page=1)

    #Extract the data
    api.get_data()

    #Create the dataframe using the function
    api.create_dataframe()

    #Counting empty cells
    missing_values = api.count_missing_values()
    print("Empty values per columns: ")
    print(missing_values)

    #Calculating total market cap
    total_market_cap = api.calculate_total_market_cap()
    print(f"Total market cap is: {total_market_cap}.")

    #Top 50 crypto currency group by the "current_price" column
    top50df = api.get_top_n("current_price", 50)
    print(f"Top 50 crypto currencies based on the 'current_price' are: ")
    print(top50df)

    #Sort based on the price change
    sorted_top50_df = api.sort_by_column("price_change_percentage_24h", ascending=False)
    print("Top 50 crypto currency based on the price change percentage: ")
    print(sorted_top50_df)

    # 7. Add new column for representing the change of the diredtion of the prices
    api.add_change_direction_column("price_change_percentage_24h", "change_direction")
    print("The DataFrame updated with the direction changed column: ")
    print(api.df.head())
