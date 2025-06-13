import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

# Function to download similarity.pkl from Google Drive
def download_file_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, destination, quiet=False)

# Cache the loading of similarity.pkl
@st.cache_resource
def load_similarity():
    if not os.path.exists("similarity.pkl"):
        FILE_ID = "14-O8APei5gpIMZqe5qWRWj4nORr2funJ"  # your Google Drive file ID
        download_file_from_google_drive(FILE_ID, "similarity.pkl")
    with open("similarity.pkl", "rb") as f:
        return pickle.load(f)

# Cache the loading of movies.pkl
@st.cache_resource
def load_movies():
    with open("movies.pkl", "rb") as f:
        return pickle.load(f)

# Load data once, with caching
similarity = load_similarity()
movies = load_movies()

# Ensure movies is a DataFrame
if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)

# Fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"

# Movie recommendation logic
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Streamlit UI
st.title('🎬 What to Watch')

selected_movie_name = st.selectbox(
    'Smart movie suggestions made just for you.',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
