from bs4 import BeautifulSoup

with open("cdCatalogue.xml",'r') as f:
    soup = BeautifulSoup(f, 'html5lib') 

title = soup.title
# print(title)
# print(title.string)
title.string = 'CD-CATALOGUE'
# print(soup.title.string)

artist = soup.find('artist')
# print(artist.string) #returns only one artist

artists = soup.find_all('artist')
# for i in artists:
#     print(i.string) 

# to access nested tag
nested_elems = soup.find('cd')
# print(nested_elems)  wont work coz we dont have any nested elements



# access from an url
import requests

url = 'https://littleboxindia.com/?ref=AC&utm_source=AC&utm_medium=AC52&utm_id=1000_652061717081d703402a212d'
result = requests.get(url)
# print(result.text)
soup = BeautifulSoup(result.text , 'html5lib')
# print(soup.prettify())

# title = soup.title
# print(title.string)


import json
with open('Books.xml','r') as file:
    data = file.read()
    # print(data)
    soup1 = BeautifulSoup(data,'xml')
    titles = soup1.find_all('title')
    soup2 = BeautifulSoup(file,'html5lib')
    authors = soup1.find_all('author')
    
dict = {}
for count,data in enumerate(titles):
    dict.update({titles[count].string:authors[count].string})
data = json.dumps(dict)
with open('Data.json','w') as file:
    json.dump(data,file)
    

    

        
    