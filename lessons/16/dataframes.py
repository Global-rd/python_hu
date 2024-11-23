import pandas as pd
import streamlit as st

st.title("Read only supermarket data")

supermarket_df = pd.read_csv("./lessons/16/test_data/supermarket_sales.csv")
st.dataframe(supermarket_df)

st.title("Editable dataframe")
editable_df = st.data_editor(supermarket_df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")