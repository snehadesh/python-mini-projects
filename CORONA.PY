# This program is to get data of corona updates all over the world
import requests
from bs4 import BeautifulSoup


country = input("Enter the country name- ")

url = 'https://www.worldometers.info/coronavirus/country/'  + country + '/'
 
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []
data_iterator = soup.find_all('div',class_= "maincounter-number" )
data.append(data_iterator)

for i in data:
    print("corona cases",i[0].text)
    print("recovered",i[1].text)
    print("Deaths",i[2].text)
  