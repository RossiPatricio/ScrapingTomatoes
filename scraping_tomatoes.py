import requests
from bs4 import BeautifulSoup

user_input = input('Title: ')
lists = user_input.split()
title = "_".join(lists)
rotten_tomatoes= "https://www.rottentomatoes.com/m/" + title

def get_description(url):
    """ Una funcion para obtener datos gentilmente de rottentomatoes.com """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description_div = soup.find('div', attrs={'slot': 'description'})
        
        if description_div:
            synopsis = description_div.find('p')
            if synopsis:
                return synopsis.text.strip()
            else:
                return description_div.text.strip()
        else:
            return "No se encontró el div con slot='description'."
    else:
        return f"No se pudo cargar la página. Código: {response.status_code}"

def get_director(movie_title):
    base_url = "https://www.rottentomatoes.com/m/"
    url = base_url + movie_title
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Error al cargar la página: {response.status_code}"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Busca cualquier etiqueta <p> que tenga class="name" y data-qa="person-name"
    director_tag = soup.find('p', class_='name', attrs={'data-qa': 'person-name'})
    if director_tag:
        return director_tag.get_text(strip=True)
    
    return "No se encontró el director."

def get_poster(movie_title):
    base_url = "https://www.rottentomatoes.com/m/"
    url = base_url + movie_title
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Error al cargar la página: {response.status_code}"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Busca el elemento <rt-img> que contiene el poster
    poster_tag = soup.find('rt-img', attrs={'slot': 'posterImage'})
    if poster_tag and poster_tag.has_attr('src'):
        return poster_tag['src']
    
    return "No se encontró el poster."

description = get_description(rotten_tomatoes)
director = get_director(title)
poster = get_poster(title)

result = f'Director: {director}\nSinopsis: {description}\nPoster path: {poster}' 

print(result)