import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# With a monthly view
# Billing per unit
# Type of best-selling product, contribution per branch
# Performance of payment methods
# How are the branch reviews?


df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df['Date'] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["month"].unique())

df_filtered = df[df[month] == month] 
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", tittle="Billing per day")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered, x="Date", y="Product Line",
                  color="City", title="Billing per type of product",
                  orientation="h")
col2.plotly_chart(fig_prod)


city_total = df.filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtered, x="City", y="Total", tittle="Billing per branch")
col3.plotly_chart(fig_city)


fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Billing per type of payment")
col4.plotly_chart(fig_kind)

city_total = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(df_filtered, y='Rating', x='City', 
                    title='Performance')
col5.plotly_chart(fig_rating, use_container_width=True)