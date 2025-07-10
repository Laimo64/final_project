# Final Project of Numerical Method - Movie Suggestion System

This is the final project for the Numerical Method course, completed in the third year of my undergraduate studies at National Cheng Kung University, Taiwan.

## Project Overview
With the rise of streaming platforms, users are often overwhelmed by the vast number of movie options. This project aims to improve the movie selection experience by developing a content-based recommendation system that suggests movies based on the user's preferred genres.

The system uses linear algebra techniques such as eigenmatrix and eigenvector computation for similarity analysis and applies user profiling to provide personalized recommendations. The user interface is built with Flet, allowing users to interact with the system through a simple GUI.

## Technologies Used
- Python with NumPy for numerical computation
- Flet for GUI development
- Linear algebra (eigen decomposition, vector projection)
- User profiling based on genre preference

## System Flow

Select Main Genre (weight = 2)
       ↓
Select Sub Genre (weight = 1)
       ↓
Compute Eigenmatrix & Eigenvector
       ↓
Project User Preference Vector
       ↓
Calculate Weighted Scores
       ↓
Apply Linear Transformation
       ↓
Display Top Recommendations via GUI


## Future Work
- Integrate web scraping to fetch up-to-date movie data
- Enable user-based collaborative filtering for more personalized results
- Add watch history tracking to improve profiling over time
