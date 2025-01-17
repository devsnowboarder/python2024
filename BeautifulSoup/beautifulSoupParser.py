
import requests
from bs4 import BeautifulSoup


url ='https://azurelib.com/azure-interview-questions-and-answers/'
response = requests.get(url)

html_content = response.content

print(html_content)


soup = BeautifulSoup(html_content, 'html.parser')
h1_tags = soup.find('h1')
print("  ")
print(h1_tags.text)
print("   ")

imags = soup.find_all('img')

for img in imags:
    print(img['src'])


mylist = soup.find('ul')

print(mylist.text)

text =  mylist.text

f = open("webScrap.txt", "w")
f.write(text)
f.close()