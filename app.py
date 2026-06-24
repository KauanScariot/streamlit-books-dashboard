import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config (layout="wide") #mantém as configurações ao carregar a página

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top100_books = pd.read_csv("datasets/top-100_trending_books.csv")

#df_reviews[df_reviews["reviewer rating"] <= 4] #retorna apenas os reviews que tem rating menor ou igual a 4
#df_top100_books[df_top100_books["book price"] < 10] #retorna apenas os top-100 books que tem preço menor que 10

price_max = df_top100_books["book price"].max() #retorna o valor máximo de book price e guarda em price_max
price_min = df_top100_books["book price"].min() #retorna o valor mínimo de book price e guarda em price_max

max_price = st.sidebar.slider("Price range", price_min, price_max, price_max) #texto é "Price_range". valores iniciam em price_min, terminam em price_max e o valor inicial é price_max
df_books = df_top100_books[df_top100_books["book price"] <= max_price] #cria um filtro dizendo que quando um preço for selecionado no slider, só poderá achar livros menores do que o valor selecionado.

df_books

fig = px.bar(df_books["year of publication"].value_counts()) #conta os valores dos anos de publicação dos livros e salva em fig, criando um gráfico de barra.
fig2 = px.histogram(df_books["book price"]) #cria um gráfico de histograma com os valores dos livros.

col1,col2 = st.columns(2) #coloca os gráficos em 2 colunas
col1.plotly_chart(fig) #monta o gráfico1
col2.plotly_chart(fig2) #monta o gráfico2