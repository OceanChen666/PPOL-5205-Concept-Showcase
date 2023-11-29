import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')

    st.write("")

    st.write("The following is the head of the `offshore_platform` dataset.")

    df = pd.read_csv("Data/Plot_data.csv")


    st.write(df)
