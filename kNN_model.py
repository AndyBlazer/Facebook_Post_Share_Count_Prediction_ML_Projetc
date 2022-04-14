import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn as sk


st.markdown('### <center><i> Predicting Facebooks post share volume <br>based on mother page like count and week day of publishing</i></center><br><br>', unsafe_allow_html=True)
#st.markdown('##### <center> Personal Challenge - Andrzej Krasnodebski', unsafe_allow_html=True)
#st.markdown('###### <center> 4146123', unsafe_allow_html=True)
#st.markdown('###### <center>  Artificial Intelligence Specialization', unsafe_allow_html=True)
#st.markdown('###### <center> <a href="https://fontys.edu/Bachelors-masters/Bachelors/Information-Communication-Technology-Eindhoven.htm">Fontys University of Applied Sciences</a>', unsafe_allow_html=True)


loaded_model = pickle.load(open('kNN_model.sav', 'rb'))

day = st.radio(
     "Select weekday of publishing",
     ('Modnay', 'Tuesday', 'Wednesday','Thursday','FridAI', 'Saturday','Sunday'))

if day == 'Modnay':
     y = 1
if day == 'Tuesday':
     y = 2
if day == 'Wednesday':
     y = 3
if day == 'Thursday':
     y = 4
if day == 'FridAI':
     y = 5
if day == 'Saturday':
    y = 6
if day == 'Sunday':
     y = 7  

st.write('You selected '+ day + ' !')


x = st.slider('How many likes does your Facebook page have ?', 0, 100000, 35600)
st.write('You selected '+ str(x) + ' likes !')


prediction = loaded_model.predict([[x,y]])*10000
prediction = int(prediction)

if st.button('Predict the share volume under this post!'):
     st.write('You can expect approximately '+ str(prediction)+' shares of your post.')