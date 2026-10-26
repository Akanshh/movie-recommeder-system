import streamlit as st
import pickle
import pandas as pd
import requests

OMDB_API_KEY = st.secrets["OMDB_API_KEY"]
PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Poster"


@st.cache_data(show_spinner=False)
def fetch_poster(title):
    try:
        response = requests.get(
            "http://www.omdbapi.com/",
            params={"apikey": OMDB_API_KEY, "t": title},
            timeout=10,
        )
        data = response.json()
        poster = data.get("Poster")
        if data.get("Response") == "True" and poster and poster != "N/A":
            return poster
    except Exception:
        pass
    return PLACEHOLDER


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_movies_poster.append(fetch_poster(title))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Name a movie to get recommendations',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)