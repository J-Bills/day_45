from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,'html.parser')

titles = soup.find_all(name='span', class_='titleline')
title_list = [title for title in titles]




scores = soup.find_all(name='span', class_='score')
score_list = [int(score.getText().replace(" points", "")) for score in scores]

highest_liked = max(score_list)
highest_liked_pos = score_list.index(highest_liked)

most_liked_article = title_list[highest_liked_pos]

article_text = most_liked_article.getText()
article_link = most_liked_article.find(name='a').get('href')



print(article_text, article_link)







###Beautiful Soup Playground###

# with open('website.html', 'r') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents,'html.parser')

# #print(soup)

# #print the first anchor tag in the html
# #print(soup.a)

# #print all of the anchor tags and return in a list
# # anchor_tags = soup.findAll(name='a')

# # for tag in anchor_tags:
# #     print(tag.getText())
    
# # heading = soup.find(name= 'h3', class_="heading")
# # print(heading.getText())
# # print(heading.get("class"))
# # print(heading.name)

# company_url = soup.select_one(selector= 'p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name.getText())

# heading = soup.select(selector='.heading')
# print(heading)
