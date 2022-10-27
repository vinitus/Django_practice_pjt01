import requests

def company():
    tmdb_file = requests.get("https://api.themoviedb.org/3/company/34?api_key=cd816292a35a17cfb6864061cec75840").json()
    tmdb_file = requests.get("https://api.themoviedb.org/3/search/company?api_key=cd816292a35a17cfb6864061cec75840&page=2").json()
    print(tmdb_file)

company()

'''
adult boolean
 
backdrop_path string or null
 
belongs_to_collection null or object
 
budget integer
 
genres array[object]
 
homepage string or null
 
id integer
 
imdb_id string or null
 
original_language string
 
original_title string
 
overview string or null
 
popularity number
 
poster_path string or null
 
production_companies array[object]
 
production_countries array[object]
 
release_date string
 
revenue integer
 
runtime integer or null
 
spoken_languages array[object]
 
status string
 
tagline string or null
 
title string
 
video boolean
 
vote_average number
 
vote_count integer
'''