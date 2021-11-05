import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open(r'C:\Users\HARSHIT\pipe.pkl', 'rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka',
 'Ireland',
 'Netherlands',
 'Zimbabwe',
 'Scotland']

cities = ['Dubai',
 'Colombo',
 'Johannesburg',
 'Mirpur',
 'Harare',
 'Auckland',
 'London',
 'Cape Town',
 'Abu Dhabi',
 'Dhaka',
 'Pallekele',
 'Barbados',
 'Wellington',
 'Durban',
 'Melbourne',
 'St Lucia',
 'Nottingham',
 'Hamilton',
 'Sydney',
 'Sharjah',
 'Centurion',
 'Lahore',
 'Chittagong',
 'Manchester',
 'Dublin',
 'Lauderhill',
 'Nagpur',
 'Southampton',
 'Edinburgh',
 'Mumbai',
 'Cardiff',
 'Mount Maunganui',
 'Kolkata',
 'Hambantota',
 'Gros Islet',
 "St George's",
 'Greater Noida',
 'Delhi',
 'Trinidad',
 'Christchurch',
 'Guyana',
 'Bready',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Ahmedabad',
 'Sylhet']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
 batting_team = st.selectbox('Select Batting Team', sorted (teams))

with col2:
 bowling_team = st.selectbox('Select Bowling Team', sorted (teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
 current_score = st.number_input('Current Score')
with col4:
 over_done = st.number_input('Overs (Only works for >5)')
with col5:
 wickets = st.number_input('Wickets left')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
 balls_left = 120 - (over_done * 6)
 wickets_left = 10 - wickets
 crr = current_score / over_done

 input_df = pd.DataFrame(
  {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
   'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
 result = pipe.predict(input_df)
 st.header("Predicted Score - " + str(int(result[0])))

