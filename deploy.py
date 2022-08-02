# Script do deploy do modelo

# Imports
import pickle
import streamlit as st
import pandas as pd
import requests

# Função que busca os posters
def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1355331d9510a8dcffa3b7afac0a3336&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path

# Função que recomenda os filmes
def sistema_recom(movie):
    index = filmes[filmes['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x: x[1])
    filmes_recom_nomes = []
    filmes_recom_poster = []

    for i in distances[1:6]:
        movie_id = filmes.iloc[i[0]].id
        filmes_recom_poster.append(get_poster(movie_id))
        filmes_recom_nomes.append(filmes.iloc[i[0]].title)

    return filmes_recom_nomes, filmes_recom_poster

st.header('Sistema de Recomendação de Filmes')
dict_filmes = pickle.load(open('Modelos/lista_filmes.pkl', 'rb'))
similarity = pickle.load(open('Modelos/similarity.pkl', 'rb'))
filmes = pd.DataFrame(dict_filmes)

movies_list = filmes['title'].values
select_movies = st.selectbox('Selecione um filme', movies_list)

if st.button('Mostrar recomendações'):
    filmes_recom_nomes, filmes_recom_poster = sistema_recom(select_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(filmes_recom_nomes[0])
        st.image(filmes_recom_poster[0])
    with col2:
        st.text(filmes_recom_nomes[1])
        st.image(filmes_recom_poster[1])
    with col3:
        st.text(filmes_recom_nomes[2])
        st.image(filmes_recom_poster[2])
    with col4:
        st.text(filmes_recom_nomes[3])
        st.image(filmes_recom_poster[3])
    with col5:
        st.text(filmes_recom_nomes[4])
        st.image(filmes_recom_poster[4])
