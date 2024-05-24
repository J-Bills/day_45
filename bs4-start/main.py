from bs4 import BeautifulSoup






###Beautiful Soup Playground###

with open('website.html', 'r') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,'html.parser')

#print(soup)

#print the first anchor tag in the html
#print(soup.a)

#print all of the anchor tags and return in a list
# anchor_tags = soup.findAll(name='a')

# for tag in anchor_tags:
#     print(tag.getText())
    
# heading = soup.find(name= 'h3', class_="heading")
# print(heading.getText())
# print(heading.get("class"))
# print(heading.name)

company_url = soup.select_one(selector= 'p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name.getText())

heading = soup.select(selector='.heading')
print(heading)
