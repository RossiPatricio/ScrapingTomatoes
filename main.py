from scraping_tomatoes import *

user_input = input('Title:')
words = user_input.split()
title = "_".join(words)

description = get_description(title)
director = get_director(title)
poster = get_poster(title)
actors = get_actors(title)

result = f'Director: {director}\nSinopsis: {description}\nStarring: {actors}\n\nPoster path: \n{poster}' 
print(result)
