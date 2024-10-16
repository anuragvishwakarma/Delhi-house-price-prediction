import pandas as pd
import streamlit as st
import pickle
import numpy as np

st.title('🐱‍🚀 Delhi NCR House Price Predictor')

st.sidebar.info('This is a Random Forest Machine Learning App.')
data = pd.read_csv('a.csv')
df = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('RF1.pkl','rb'))

st.sidebar.markdown("Select Below Parameters 😄")


city = st.sidebar.selectbox('City', df['City'].unique())
area = st.sidebar.number_input('Area sqft')
bedroom = st.sidebar.selectbox('Bedrooms', df['Bedrooms'].unique())
bathroom = st.sidebar.selectbox('Bathrooms', df['Bathrooms'].unique())
building = st.sidebar.selectbox('Type of building', df['type_of_building'].unique())
status = st.sidebar.selectbox('Status',df['Status'].unique())
neworold = st.sidebar.selectbox('New or Old Property',df['neworold'].unique())


if st.sidebar.button('Predict Price'):

    if status == 'Under Construction':
        status = 1
    else:
        status = 0

    if building == "Individual House":
        building = 1
    else:
        building = 0

    if neworold == "Resale":
        neworold = 1
    else:
        neworold = 0
    
    if city == "Faridabad":
        city = 0    
    elif city == "Ghaziabad":
        city = 1
    elif city == "Greater Noida":
        city = 2
    elif city == "Gurgaon":
        city = 3
    elif city == "Gurgaon - North":
        city = 4
    elif city == "Gurgaon - South":
        city = 5
    elif city == "New Delhi":
        city = 6
    elif city == "New Delhi - Central":
        city = 7
    elif city == "New Delhi - Dwarka":
        city = 8
    elif city == "New Delhi - East":
        city = 9
    elif city == "New Delhi - North":
        city = 10
    elif city == "New Delhi - Rohini":
        city = 11
    elif city == "New Delhi - South":
        city = 12
    elif city == "New Delhi - West":
        city = 13
    elif city == "Noida":
        city = 14
    
    query = np.array([area,bedroom,bathroom,status,neworold,building,city])
    query = query.reshape(1,7)
    st.title("The predicted price for the selected house is ₹"+str(int(model.predict(query))))

st.sidebar.write('Made with ❤️ by [Anurag Vishwakarma](https://www.linkedin.com/in/anurag2407/)')

data = data[['latitude','longitude']]
#noida = (28.5355, 77.3910)
#map = folium.map(location=noida, zoom_start=9)
#st_folium(map, width=700)

st.map(data, size=10)


