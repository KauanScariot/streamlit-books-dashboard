import streamlit as st
import pandas as pd

st.set_page_config (layout="wide") #mantém as configurações ao carregar a página

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top100_books = pd.read_csv("datasets/top-100_trending_books.csv")

books = df_top100_books["book title"].unique() #separa os títulos, um a um.
book = st.sidebar.selectbox("Selecione um livro", books) #cria um selectbox na sidebar

df_book = df_top100_books[df_top100_books["book title"] == book] #retorna o livro quando ele tem o mesmo nome selecionado no input de book
df_reviews_f = df_reviews[df_reviews["book name"] == book] #retorna uma lista de reviews quando ele tem o mesmo nome selecionado no input de book

# Pega o título do livro da coluna "book title"
# .iloc[0] significa: pegar a PRIMEIRA linha encontrada
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Mostra o título grande na página, e o gênero abaixo.
st.title(book_title)
st.subheader(book_genre)

#divide em 3 colunas e 
# Mostra uma métrica dentro da coluna 1. Exemplo: Price $20
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year", book_year)

st.divider()

# Percorre todas as linhas do dataframe de reviews
# .values transforma as linhas em listas
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])

