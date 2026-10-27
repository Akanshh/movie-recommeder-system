# 🎬 Movie Recommender System

A content-based movie recommender built with Python and Streamlit. Pick a movie you like and the app suggests 5 similar movies, along with their posters.

**Live demo:** https://movie-recommeder-system-20.streamlit.app

## How it works

1. The movie data comes from the **TMDB Movies dataset**.
2. Each movie's metadata (overview, genres, keywords, cast, crew) is combined into a single "tags" text.
3. The tags are converted into vectors, and **cosine similarity** is calculated between every pair of movies.
4. When you select a movie, the app finds the 5 movies with the highest similarity scores.
5. Posters are fetched live from the **OMDb API**.

## Tech stack

- Python
- Streamlit
- Pandas, NumPy
- scikit-learn (cosine similarity)
- OMDb API (posters)

## Run locally

```bash
git clone https://github.com/akanshh/movie-recommeder-system.git
cd movie-recommeder-system
pip install -r requirements.txt
```

Create a file `.streamlit/secrets.toml` and add your OMDb API key (get a free one at https://www.omdbapi.com/apikey.aspx):

```toml
OMDB_API_KEY = "your_key_here"
```

Then start the app:

```bash
streamlit run app.py
```

## Project structure

```
├── app.py               # Streamlit app
├── movie_dict.pkl       # Movie titles and data
├── similarity.pkl       # Precomputed similarity matrix
└── requirements.txt     # Dependencies
```

## Author

Made by **Akanshh**