import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # kita buat judul
    st.title('Flight Price Prediction')

    st.write('Arif Imam Fauzi - Batch 30 Remote')

    # tambah gambar
    image = Image.open('flight_ticket_prices.jpeg')
    st.image(image, caption= 'Flight Ticket Price')

    # sub header
    st.subheader(''' :rainbow[Exploratory Data Analysis of Flight Price] ''')

    # buat garis lurus/pemisah
    st.markdown('---')

    # kita buat teks
    multi = '''Dibagian ini, kita akan fokus dalam menampilkan visualisasi dari beberapa bagian yang berkaitan dengan _Flight Price_.
    Untuk itu, kita bisa pilih visualisasi yang akan ditampilkan. Dataset yang digunakan bisa dilihat dibawah ini.
    '''
    st.markdown(multi)

    # tampilkan dataframe
    data = pd.read_csv('flight_price.csv')
    st.dataframe(data)

    # function untuk menampilkan nilai pada label
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i,y[i],y[i])

    # histogram pilihan user (memilih)
    st.write('## Visualisasi Dataset')
    option = st.selectbox('Pilih kolom: ', ('baseFare vs totalFare', 'Flight Mode', 'Base Type Ticket', 'Top 5 Airport', 'Day of Departure'))

    if option == 'baseFare vs totalFare':
        # jika kita lihat dari sebaran baseFare dan totalFare
        fig = plt.figure(figsize=(15, 8))

        # kita tampilkan plot distribution dari baseFare
        plt.subplot(1, 2, 1)
        sns.histplot(data['baseFare'], kde=True, bins=60)
        plt.title('Distribution of Basic Price')

        # kita tampilkan plot untuk totalFare
        plt.subplot(1, 2, 2)
        sns.histplot(data['totalFare'], kde=True, bins=60)
        plt.title('Distribution of Total Price')

        # tampilkan plot
        st.pyplot(fig)
    
    elif option == 'Flight Mode':
        fig_2 = plt.figure(figsize=(15,8))

        # kita definisikan warna
        colors = sns.color_palette('pastel')[0:5]

        # kita buat variabel lain untuk menyimpan nama label dalam diagram
        label = ['Transit', 'Non-Stop']

        # kita buat diagram lingkarannya dengan variabel warna dan label yang telah kita buat
        plt.pie(data['isNonStop'].value_counts(), labels = label, colors = colors, autopct='%.2f%%')
        plt.title('Flight Mode')
        # tampilkan plot
        st.pyplot(fig_2)

    elif option == 'Base Type Ticket':
        fig_3 = plt.figure(figsize=(15,8))
        
        # kita definisikan warna
        colors = sns.color_palette('pastel')[3:6]

        # kita buat variabel lain untuk menyimpan nama label dalam diagram
        label = ['Non-Basic', 'Basic']

        # kita buat diagram lingkarannya dengan variabel warna dan label yang telah kita buat
        plt.pie(data['isBasicEconomy'].value_counts(), labels = label, colors = colors, autopct='%.2f%%')
        plt.title('Type of Flight Ticket')
        
        # kita tampilkan plot
        st.pyplot(fig_3)

    elif option == 'Top 5 Airport':
        fig_4 = plt.figure(figsize=(15,8))

        # kita buat label untuk posisi x pada kedatangan dan keberangkatan
        departure = ['LAX', 'BOS', 'LGA', 'ORD', 'SFO']
        arrival = ['LAX', 'LGA', 'DFW', 'MIA', 'BOS']

        # Membuat bar plot
        plt.subplot(1, 2, 1)
        plt.bar(departure, data['startingAirport'].value_counts().sort_values(ascending=False).head(), color=sns.color_palette('pastel')[0:5])
        addlabels(departure, data['startingAirport'].value_counts().sort_values(ascending=False).head())

        # Memberikan label sumbu-x dan sumbu-y
        plt.xlabel('Airport Code')
        plt.ylabel('Count')
        plt.title('Top 5 Departure Airport', )

        plt.subplot(1, 2, 2)
        plt.bar(arrival, data['destinationAirport'].value_counts().sort_values(ascending=False).head(), color=sns.color_palette('pastel')[3:8])
        addlabels(arrival, data['destinationAirport'].value_counts().sort_values(ascending=False).head())

        # Memberikan label sumbu-x dan sumbu-y
        plt.xlabel('Airport Code')
        plt.ylabel('Count')
        plt.title('Top 5 Arrival Airport', )

        # kita tampilkan plot
        st.pyplot(fig_4)

    elif option == 'Day of Departure':
        fig_5 = plt.figure(figsize=(15,8))

        # kita buat label untuk posisi x
        categories = ['Same Day', 'Different Day']

        # Membuat bar plot
        plt.bar(categories, data['elapsedDays'].value_counts(), color=sns.color_palette('deep'))
        addlabels(categories, data['elapsedDays'].value_counts())

        # Memberikan label sumbu-x dan sumbu-y
        plt.xlabel('Travel Day')
        plt.ylabel('Count')
        plt.title('Arrival Day')

        # kita tampilkan plot
        st.pyplot(fig_5)


if __name__ == '__main__':
    run()