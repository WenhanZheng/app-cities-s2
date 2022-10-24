import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
plt.style.use('seaborn')
st.title('World Cities by Amanda')
df=pd.read_csv('worldcities.csv')
#add a slider
pop_filter = st.sidebar.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)
#filter by population
df = df[df.population >= pop_filter]
#add a capital select filter
capital_filter=st.sidebar.multiselect('capital select', df.capital.unique(),['primary','admin'])
df=df[df.capital.isin(capital_filter)]
# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")
# filter by capital
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]
#地图
st.map(df)
#表格 
st.write(df)
#柱状图
fig,ax=plt.subplots()
pop_sum=df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)