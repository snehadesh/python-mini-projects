#this program is to get top 10 news of your area of interest from the website of times of india.
import requests
from bs4 import BeautifulSoup


print("Hello user! find the news related to your interest here.")
selected_tag = input("select tag - Education/Business/politics ")
print(selected_tag)
URL = 'https://timesofindia.indiatimes.com/' + selected_tag

page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find_all('span',class_="w_tle")
listof = []
for title in results:
    #print(title, end='\n'*2)
    news= title.find('a')
    listof.append(news)
#print(listof)
n = 1       
for i in listof[:10]:
    print((str(n) + '.'), i.text)
    n += 1
    if None in (listof):
        continue






