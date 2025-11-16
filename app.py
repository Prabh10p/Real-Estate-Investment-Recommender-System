import pandas as pd
import numpy as np
import streamlit as st
import pickle




df = pickle.load(open('/Users/prabhsandhu/Real-Estate-Investment-Recommender-System/Artifacts/Model/df.pkl','rb'))
city_options = sorted(df['city'].astype(str).unique().tolist())
state_options = sorted(df['state'].astype(str).unique().tolist())
status_options = sorted(df['status'].astype(str).unique().tolist())
min_price = int(df["price"].min())
max_price = int(df["price"].max())
median = int(df["price"].median())
# bed
# acre_lot
# zip_code
# house_size
st.header("Real Estate Recommender System")
city = st.selectbox("Select City",city_options)
state = st.selectbox("Select State",state_options)
status_options = st.selectbox("Select Status",status_options)
price = st.slider("Select Price",min_value=min_price,max_value=max_price)
new_house = {
    'city': 'Ponce',
    'state': 'Florida',
    'status': 'for_sale',
    'price': 96000,
    'bed': 3,
    'bath': 2,
    'acre_lot': 1,
    'zip_code': 728,
    'house_size': 1200
}








