import pandas as pd 
import streamlit as st

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

st.dataframe(df)
