#this program is to get blogs with links from medium.com 
import requests
from bs4 import BeautifulSoup

print("Hello,find your desired job here!")
keyword= input("Enter the BLOG title you are searching for-  ")
print(keyword)

URL = 'https://medium.com/search?q=' + keyword
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find_all('div',class_="postArticle-content")
link_of = soup.find_all("a", href=True)
list_of = []
for blog in results:
    blog_list= blog.find('h3')
    list_of.append(blog_list)
n = 1    
for i in list_of:
    if i == None:
        continue
    for el in link_of:
        link =el['href']
    print((str(n) + '.'),i.text)
    n += 1
    print("Link --",link,end='\n'*2)
   
        

    