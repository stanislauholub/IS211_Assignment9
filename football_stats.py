#!/usr/bin/env python
# coding: utf-8

# In[73]:


# PART I: CBS Football Stats

from bs4 import BeautifulSoup as bs4
import requests

URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'

data = []
r = requests.get(URL)
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')
table = soup.find('table', attrs = {'class': 'data'})

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')#[:3][-19:-12]
    columns = [elements.text.strip() for elements in columns]
    data.append([elements for elements in columns if elements])
    
data = data[3:23]

print(len(data), "TOP NFL PLAYERS WITH MOST NUMBERS OF TOUCHDOWNS:\n")

for i in range(len(data)):
    print(data[i][0], ":", data[i][1], data[i][2], data[i][6])


# In[ ]:
