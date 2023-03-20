from bs4 import BeautifulSoup
import requests, re

data = requests.get('http://scp-wiki.wikidot.com/scp-series/').content
soup = BeautifulSoup(data, 'lxml')

tags = soup.find(name="div",class_='content-panel standalone series')

# save data get to an txt file
with open('scpWIKI.txt', 'w', encoding='utf-8') as f:
    f.write('All information are from SCP wiki'+ '\n')
    for li in tags:
        a = li.find("li")
        f.write('' + li.text + '\n')
