#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:54:50 2024

@author: bouba
"""

# import the necessary libraries 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset movie_dataset
movie_data=pd.read_csv('movie_dataset.csv')
movie_data.head()

#Number of columns and observations
movie_data.shape

# Summary of a dataset 
movie_data.info()

# Descriptive Statistics
print(movie_data.describe())

# Number of Null values by columns
movie_data.isnull().sum()

#### Question 1
# What is the highest rated movie in the dataset?
# Find the row with the maximum rating
highest_rated_movie = movie_data[movie_data['Rating'] == movie_data['Rating'].max()]
# Print the result
print("Highest Rated Movie:")
print(highest_rated_movie[['Rank', 'Title', 'Rating']])


#### Question 2 (Method 1 )
#What is the average revenue of all movies in the dataset? 
#Note, since the answer will be effected by how you dealt with missing values a range has been provided. 
# Replace any missing values in the 'Revenue (Millions)' column with 0
movie_data['Revenue (Millions)'].fillna(0, inplace=True)
# Calculate the average revenue
average_revenue = movie_data['Revenue (Millions)'].mean()
# Print the result
print("Average Revenue of All Movies:")
print(average_revenue)

#### Question 2 (Method 2)
# Calculate the mean of the 'Revenue (Millions)' column
mean_revenue = movie_data['Revenue (Millions)'].mean()
# Replace missing values with the mean
movie_data['Revenue (Millions)'].fillna(mean_revenue, inplace=True)
# Calculate the average revenue
average_revenue = movie_data['Revenue (Millions)'].mean()
# Print the result
print("Average Revenue of All Movies:")
print(average_revenue)


#### Question 3
#What is the average revenue of movies from 2015 to 2017 in the dataset?
#Note, since the answer will be effected by how you dealt with missing values a range has been provided. 
# Filter the dataset for movies from 2015 to 2017
filtered_movies = movie_data[(movie_data['Year'] >= 2015) & (movie_data['Year'] <= 2017)]
# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_movies['Revenue (Millions)'].mean()
# Print the result
print("Average Revenue of Movies from 2015 to 2017:")
print(average_revenue_2015_to_2017)

##### Question 4
# How many movies were released in the year 2016?
# Filter the dataset for movies released in the year 2016
movies_2016 = movie_data[movie_data['Year'] == 2016]
# Get the count of movies released in 2016
num_movies_2016 = len(movies_2016)
# Print the result
print("Number of Movies Released in the Year 2016:")
print(num_movies_2016)


##### Question 5
# How many movies were directed by Christopher Nolan?
# Filter the dataset for movies directed by Christopher Nolan
nolan_movies = movie_data[movie_data['Director'] == 'Christopher Nolan']
# Get the count of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)
# Print the result
print("Number of Movies Directed by Christopher Nolan:")
print(num_nolan_movies)

#### Question 6
# How many movies in the dataset have a rating of at least 8.0?
# Filter the dataset for movies with a rating of at least 8.0
high_rated_movies = movie_data[movie_data['Rating'] >= 8.0]
# Get the count of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)
# Print the result
print("Number of Movies with a Rating of at Least 8.0:")
print(num_high_rated_movies)

#### Question 7
# What is the median rating of movies directed by Christopher Nolan?
# Filter the dataset for movies directed by Christopher Nolan
nolan_movies = movie_data[movie_data['Director'] == 'Christopher Nolan']
# Calculate the median rating for movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()
# Print the result
print("Median Rating of Movies Directed by Christopher Nolan:")
print(median_rating_nolan_movies)

#### Question 8
# Find the year with the highest average rating?
# Group the dataset by the 'Year' and calculate the average rating for each year
average_rating_by_year = movie_data.groupby('Year')['Rating'].mean()
# Find the year with the highest average rating
year_highest_avg_rating = average_rating_by_year.idxmax()
# Print the result
print("Year with the Highest Average Rating:")
print(year_highest_avg_rating)


#### Question 9
### What is the percentage increase in number of movies made between 2006 and 2016?
# Filter the dataset for movies made in 2006 and 2016
movies_2006 = movie_data[movie_data['Year'] == 2006]
movies_2016 = movie_data[movie_data['Year'] == 2016]
# Calculate the number of movies made in each year
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)
# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
# Print the result
print("Percentage Increase in Number of Movies between 2006 and 2016:")
print(percentage_increase)


#### Question 10
#Find the most common actor in all the movies?
#Note, the "Actors" column has multiple actors names. You must find a way to search for the most common actor in all the movies.
# Split the 'Actors' column to get individual actor names
all_actors = movie_data['Actors'].str.split(', ')
# Flatten the list of lists into a single list of all actor names
all_actors_flat = [actor for sublist in all_actors for actor in sublist]
# Create a pandas Series from the list of actors
actors_series = pd.Series(all_actors_flat)
# Find the most common actor
most_common_actor = actors_series.mode()[0]
# Print the result
print("Most Common Actor in All Movies:")
print(most_common_actor)


##### Question 11
#How many unique genres are there in the dataset?
#Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.
# Split the 'Genre' column to get individual genre names
all_genres = movie_data['Genre'].str.split(',')
# Flatten the list of lists into a single list of all genre names
all_genres_flat = [genre.strip() for sublist in all_genres for genre in sublist]
# Create a set from the list of genres to get unique genres
unique_genres = set(all_genres_flat)
# Get the count of unique genres
num_unique_genres = len(unique_genres)
# Print the result
print("Number of Unique Genres in the Dataset:")
print(num_unique_genres)


##### Question 12
# Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.
#And what advice can you give directors to produce better movies?
# Selecting numerical features for correlation analysis
numerical_features = movie_data[['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]
# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()
# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)


## heatmap
import seaborn as sns
plt.figure(figsize=(8,5))
sns.heatmap(correlation_matrix, annot=True)



































