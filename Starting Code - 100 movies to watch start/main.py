import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

movie_webpage = response.text

soup =BeautifulSoup(movie_webpage, 'html.parser')

number_title_list_html = soup.find_all(name='h3', class_='title')

num_list_text = [contents.getText() for contents in number_title_list_html]

movie_list = list()
for i in range(len(num_list_text)-1,-1,-1):
    movie_list.append(num_list_text[i]+ '\n')

with open('movies.txt', 'w') as movie_file:
    movie_file.writelines(movie_list)