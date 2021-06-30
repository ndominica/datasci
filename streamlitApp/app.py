import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache
def read_data(data_loc):
    data = pd.read_csv(data_loc)
    data['week'] = data.year_week.apply(lambda x:convert(x))
    return data
    

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54
    return year + int(week)


# Data
data = read_data('data/csv')
list_of_countries = list(set(data['country']))
list_of_countries.sort(reverse=False)


# Gui
st.title("Worldwide Covid-19 Trends")
country = st.selectbox('Select a country', list_of_countries)
st.write('The selected country is {}'.format(country))


# Gui filled with data
country_data = data[data.country == country]
fig = px.line(data_frame=country_data, x ='week', y='cumulative_count', color='indicator')
st.plotly_chart(fig)