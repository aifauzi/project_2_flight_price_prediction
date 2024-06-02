import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('Exploratory Data', 'Prediction'))

if page == 'Exploratory Data':
    eda.run()
else:
    prediction.run()