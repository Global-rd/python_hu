import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime

API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "https://api.polygon.io/v2/aggs/ticker"

@st.cache_data(ttl=86400)
def fetch_stock_data(symbol):
    print(f"Fetch data for {symbol}")

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")

    url = f"{BASE_URL}/{symbol}/range/1/day/{start_date_str}/{end_date_str}"

    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
    
st.title("Stock Market Dashboard")
st.sidebar.header("Configuration")

stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g.: AAPL, TSLA, MSFT)", "AAPL")

data = fetch_stock_data(stock_symbol)
print(data)

def process_data(data):

    if 'results' in data:
        df = pd.DataFrame(data["results"])
        df["timestamp"] = pd.to_datetime(df['t'], unit="ms")
        df.set_index('timestamp', inplace=True)
        df = df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"})
        df = df.drop(columns={"t", "vw", "n"})
        df = df.sort_index()
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
        df[numeric_columns] = df[numeric_columns].astype(float)
        print(df)
        return df
    else:
        st.error("No data available.")
        return None

    
if data:
    df = process_data(data)
    st.header(f"Stock overview: {stock_symbol.upper()}")

    if df is not None:
        kpi1, kpi2, kpi3 = st.columns(3)
        #KPI
        with kpi1:
            st.metric(label="Latest Closing Price", value=f"${df['Close'].iloc[-1]:.2f}")
        with kpi2:
            st.metric(label="Volume", value=f"{df['Volume'].iloc[-1]:,.2f}")
        with kpi3:
            st.metric(label="Highest Price (Last 30 Days)", value=f"${df['High'][-30:].max():.2f}")

        #LINE CHART:
        st.subheader("Closing Price Over Time")
        fig_close = px.line(df, x=df.index, y="Close", title=f"{stock_symbol.upper()} Closing Price Over Time")
        st.plotly_chart(fig_close)

        #BAR CHART:
        st.subheader("Trading Volume Over Time")
        fig_volume = px.bar(df, x=df.index, y="Volume", title=f"{stock_symbol.upper()} Trading Volume Over Time")
        st.plotly_chart(fig_volume)
        
        #raw data
        st.subheader("Raw data")
        st.write(df)
else:
    st.error("No data available. Check the symbol.")