import pickle
import streamlit as st
import requests
import os


def fetch_poster(movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        return None
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(
            movie_id, api_key
        )
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        poster_path = data.get("poster_path")
        if not poster_path:
            return None
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception:
        return None


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_row = movies.iloc[i[0]]
        movie_id = movie_row.get("movie_id") or movie_row.get("id")
        poster_url = None
        if movie_id is not None:
            poster_url = fetch_poster(movie_id)
        recommended_movie_posters.append(poster_url)
        recommended_movie_names.append(movie_row.title)

    return recommended_movie_names, recommended_movie_posters


st.header("Movie Recommender System")
movies = pickle.load(open("models/movie_list.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            poster = recommended_movie_posters[idx]
            if poster:
                st.image(poster)
            else:
                st.write("No poster available")
