import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# load file & model
# kita load model dan file yang kita butuhkan
 
with open('list_num_cols.txt', 'r') as file_1:
  list_num_col = json.load(file_1)

with open('list_cat_cols_enc.txt', 'r') as file_2:
  list_cat_col_enc = json.load(file_2)

with open('standard_scaler.pkl', 'rb') as file_3:
  scaler = pickle.load(file_3)

with open('ohe_encoder.pkl', 'rb') as file_4:
  enc_ohe = pickle.load(file_4)

with open('model_regresi.pkl', 'rb') as file_5:
  model_ridge = pickle.load(file_5)

with open('list_cat_cols_notenc.txt', 'r') as file_6:
  list_cat_col_notenc = json.load(file_6)

def run():
  
  with st.form('form_flight_price'):
    # input bandara awal
    start_airport = st.selectbox('Pilih bandara Anda berangkat', ('EWR', 'BOS', 'DEN', 'ORD', 'IAD', 'OAK', 'SFO', 'LGA', 'PHL', 'CLT', 'DTW', 'DFW', 'ATL', 'MIA', 'LAX', 'JFK'), index = 1)

    # input bandara tujuan
    destination_airport = st.selectbox('Pilih bandara tujuan Anda', ('EWR', 'BOS', 'DEN', 'ORD', 'IAD', 'OAK', 'SFO', 'LGA', 'PHL', 'CLT', 'DTW', 'DFW', 'ATL', 'MIA', 'LAX', 'JFK'), index = 0)

    # input hari yang dihabiskan
    wasting_day = st.selectbox('Apakah sampai berganti hari?', (0, 1), index = 0, help = '0 = Tidak, 1 = Ya')
    
    # input basic ticket
    basic = st.selectbox('Apakah tiket Anda _Basic Economy_?', (0, 1), index = 0, help = '0 = Tidak, 1 = Ya')
    
    # input status refund
    refund = st.selectbox('Apakah tiket Anda _Refundable_?', (0, 1), index = 0, help = '0 = Tidak, 1 = Ya')

    # input status perjalanan non-stop
    nonstop = st.selectbox('Apakah Anda melakukan perjalanan _Non-Stop_?', (0, 1), index = 0, help = '0 = Tidak, 1 = Ya')

    # input harga dasar
    base = st.number_input('Inputkan harga dasar yang ditawarkan', value = 0, min_value = 0)

    # input jumlah kursi tersisa
    seat = st.number_input('Inputkan jumlah kursi yang tersisa', value = 0, min_value = 0)

    # input jarak perjalanan
    travel_distance = st.number_input('Inputkan total jarak perjalanan Anda', value = 0, min_value = 0)

    # input selisih hari pemesanan dan hari keberangkat
    order = st.number_input('Inputkan jarak hari pemesanan tiket Anda dengan jadwal keberangkatan', value = 0, min_value = 0)
    
    # inputkan bulan keberangkatan
    month = st.number_input('Inputkan bulan keberangkatan Anda', value = 1, min_value = 1, max_value = 12)

    # inputkan waktu perjalanan
    travel_duration = st.number_input('Inputkan total waktu perjalanan Anda', value = 0, min_value = 0)

    # inputkan jam ketika tiba di bandara pertama
    hour_departure = st.number_input('Inputkan jam kedatangan Anda di bandara pertama', value = 0, min_value = 0, max_value = 23, help = '0 = 24')

    # inputkan kode maskapai keberangkatan pertama
    airline = st.selectbox('Inputkan kode maskapai pesawat Anda pada kebrangkatan pertama?', ('AA', 'DL', 'UA', 'F9', 'B6', 'AS', '9X', 'SY', '9K', '4B', 'KG'), index = 0)

    # inputkan jumlah penerbangan
    sumflight = st.number_input('Inputkan total penerbangan Anda', value = 1, min_value = 1, max_value = 4)

    # inputkan lamanya waktu penerbangan
    dur_flight = st.number_input('Inputkan total waktu penerbangan Anda', value = 0, min_value = 0)

    # inputkan musim saat keberangkatan
    season = st.selectbox('Inputkan musim saat keberangkatan Anda?', ('spring', 'summer'), index = 0)

    # inputkan tipe kabin
    cabin = st.selectbox('Inputkan musim saat keberangkatan Anda?', ('coach', 'premium coach', 'business', 'first'), index = 0)

    # inputkan waktu menunggu transit
    waiting = st.number_input('Inputkan total waktu Anda menunggu ketika transit', value = 0, min_value = 0)

    # submit button
    submit = st.form_submit_button('Predict')

  data_inf = {
    'startingAirport': start_airport,
    'destinationAirport': destination_airport,
    'elapsedDays': wasting_day,
    'isBasicEconomy': basic,
    'isRefundable': refund,
    'isNonStop': nonstop,
    'baseFare': base,
    'seatsRemaining': seat,
    'totalTravelDistance': travel_distance,
    'orderingDistance': order,
    'monthDeparture': month,
    'travelDurationInMinutes': travel_duration,
    'firstHourDeparture': hour_departure,
    'firstDepartureAirlineCode': airline,
    'sumFlight': sumflight,
    'durationFlightInMinutes': dur_flight,
    'seasonDeparture': season,
    'firstCabinCode': cabin,
    'totalWaitingTimeTransit': waiting
    }

  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)

  # kita buat kondisi dimana predik baru bisa dilakukan ketika kita klik Predict
  if submit:
    
    # kita split data yang bersifat numerik (untuk scaling) dan kategorik (ada yang untuk encoding dan tidak)
    data_inf_num = data_inf[list_num_col]
    data_inf_cat_enc = data_inf[list_cat_col_enc]
    data_inf_cat_notenc = data_inf[list_cat_col_notenc]

    # kita lakukan scaling dan encoding
    data_inf_num_scaled = scaler.transform(data_inf_num)
    data_inf_cat_encoded = enc_ohe.transform(data_inf_cat_enc).toarray()
    data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded, data_inf_cat_notenc], axis = 1)

    # kita jadikan ke dataframe
    data_inf_df = pd.DataFrame(data_inf_final, columns=[list_num_col + list(enc_ohe.get_feature_names_out()) + list_cat_col_notenc])
    data_inf_df = data_inf_df.drop(['orderingDistance', 'firstHourDeparture'], axis=1)

    # kita lakukan predict dengan Ridge
    y_pred_inf = model_ridge.predict(data_inf_df)

    # kita munculkan hasilnya
    st.write('## Prediksi harga tiket Anda : ', y_pred_inf)


if __name__ == '__main__':
  run()