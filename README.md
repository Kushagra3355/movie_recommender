# Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit that suggests similar movies based on your selection.
Live DEMO: https://movies-recommendat.streamlit.app/

## Features

- Browse and select from thousands of movies
- Get 5 personalized movie recommendations based on similarity
- Display movie posters (requires TMDB API key)
- Fast and responsive web interface

## Demo

Select a movie from the dropdown, click "Show Recommendation", and get 5 similar movie suggestions!

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Kushagra3355/movie_recommender.git
cd movie_recommender
```

2. Install required dependencies:

```bash
pip install streamlit requests python-dotenv
```

3. Set up TMDB API key (optional, for poster images):
   - Get your free API key from [TMDB](https://www.themoviedb.org/settings/api)
   - Create a `.env` file in the project root:
   ```
   TMDB_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How It Works

1. **Content-Based Filtering**: The system uses movie features (genres, keywords, cast, crew) to calculate similarity between movies
2. **Cosine Similarity**: Recommendations are based on cosine similarity scores computed from movie metadata
3. **Pre-trained Model**: The similarity matrix is pre-computed and stored in `similarity.pkl` for fast recommendations

## Project Structure

```
movie_recommender/
├── app.py                      # Streamlit web application
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── data/                       # Dataset directory
│   ├── tmdb_5000_movies.csv    # Movie dataset
│   └── tmdb_5000_credits.csv   # Movie credits dataset
├── models/                     # Model files directory
│   ├── movie_list.pkl          # Preprocessed movie data
│   └── similarity.pkl          # Pre-computed similarity matrix
└── notebooks/                  # Jupyter notebooks
    └── model.ipynb             # Jupyter notebook for model training
```

## Technologies Used

- **Python** - Programming language
- **Streamlit** - Web framework for the UI
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning library
- **Requests** - API calls for movie posters
- **TMDB API** - Movie poster images

## Dataset

This project uses the TMDB 5000 Movie Dataset containing:

- Movie metadata (genres, keywords, overview)
- Cast and crew information
- 4800+ movies

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
