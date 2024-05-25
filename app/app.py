import streamlit as st
import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code == 200:
    data = json.loads(response.text)
    
    number_of_people = data['number']
    people = data['people']
else:
    number_of_people = 0
    people = []

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        location = {"LATITUDE": [float(data['iss_position']['latitude'])], "LONGITUDE": [float(data['iss_position']['longitude'])]}
        return location
    else:
        st.error("Failed to retrieve ISS location")

#----------------------------------------------------------------------------------------------------------------------

st.title("People Currently in Space")
st.markdown("""
This application is divided in two: the first part showcases the number of people currently in space and their names while the second part showcases the current location of the International Space Station.
            """)
st.markdown("""
1. This application fetches real-time data about the number of people currently in space and their names using the Open Notify API.
""")

st.header(f"Number of People in Space: {number_of_people}")

st.subheader("Names of People in Space:")
for person in people:
    st.write(person['name'])

st.title("ISS Tracker")
st.markdown("""
2. This application fetches the current location of the International Space Station (ISS) using the Open Notify API and visualizes it on a map.
""")

location = get_iss_location()
if location:
    st.header("Current ISS Location")
    st.map(location)
    st.markdown("The marker represents the current location of the International Space Station.")
else:
    st.write("Unable to retrieve ISS location at the moment.")

st.markdown("----- Made by Freddy Mercado for his Enterprise Architectures for Big Data course -----")
