import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data: each movie has a title, actors, genre, release year, and tags
movies = [
    {"title": "Inception", "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt", "genre": "Sci-Fi", "year": "2010", "tags": "dream, heist, mind-bending"},
    {"title": "The Matrix", "actors": "Keanu Reeves, Laurence Fishburne", "genre": "Sci-Fi", "year": "1999", "tags": "virtual reality, action, hacker"},
    {"title": "The Dark Knight", "actors": "Christian Bale, Heath Ledger", "genre": "Action", "year": "2008", "tags": "superhero, crime, Gotham"},
    {"title": "Interstellar", "actors": "Matthew McConaughey, Anne Hathaway", "genre": "Sci-Fi", "year": "2014", "tags": "space, time, black hole"},
    {"title": "Pulp Fiction", "actors": "John Travolta, Samuel L. Jackson", "genre": "Crime", "year": "1994", "tags": "gangsters, nonlinear, dialogue"},
    {"title": "Fight Club", "actors": "Brad Pitt, Edward Norton", "genre": "Drama", "year": "1999", "tags": "anarchy, psychological, split personality"},
    {"title": "The Shawshank Redemption", "actors": "Tim Robbins, Morgan Freeman", "genre": "Drama", "year": "1994", "tags": "prison, hope, friendship"},
    {"title": "The Godfather", "actors": "Marlon Brando, Al Pacino", "genre": "Crime", "year": "1972", "tags": "mafia, family, crime"},
    {"title": "Gladiator", "actors": "Russell Crowe, Joaquin Phoenix", "genre": "Action", "year": "2000", "tags": "revenge, Rome, combat"},
    {"title": "Titanic", "actors": "Leonardo DiCaprio, Kate Winslet", "genre": "Romance", "year": "1997", "tags": "shipwreck, love, historical"}
]

# Convert the list of movies into a DataFrame
df = pd.DataFrame(movies)

# Create a new feature that combines all the relevant information
df['combined_features'] = df['actors'] + ' ' + df['genre'] + ' ' + df['year'] + ' ' + df['tags']

# Display the DataFrame
print("Movie Dataset:")
print(df[['title', 'combined_features']], "\n")

# Create a TF-IDF Vectorizer to transform the text data
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend similar movies
def recommend_movies(movie_title, cosine_sim=cosine_sim):
    if movie_title not in df['title'].values:
        print("Movie not found in the database.")
        return
    
    # Get the index of the movie that matches the title
    idx = df.index[df['title'] == movie_title][0]
    
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the 5 most similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:6]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Print the recommended movies
    print(f"Movies similar to '{movie_title}':")
    for i in movie_indices:
        print(f"- {df['title'].iloc[i]}")

# User input for movie recommendation
movie_to_search = input("Enter a movie title to get recommendations: ")
recommend_movies(movie_to_search)
