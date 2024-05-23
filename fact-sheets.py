from bs4 import BeautifulSoup
import requests
import json

url = "https://www.af.mil/About-Us/Fact-Sheets/?Page="
data = []

for i in range(1, 12):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for div in soup.find_all('div', {'class': 'thumb'}):
        a_tag = div.find('a')
        link = a_tag['href']
        links.append(link)

    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        title = soup.find('article').find('header').find('h1').text.strip()
        description = soup.find('article').find('section').text.strip()
    
        data.append({"url":link, "title":title, "description":description})
    
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)