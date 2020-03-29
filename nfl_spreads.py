#!/usr/bin/env python
# coding: utf-8

# In[48]:


# PART II: NFL (I have decided to try this one out as well)

from bs4 import BeautifulSoup as bs4
import requests

URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"

data = []
r = requests.get(URL)
html_bytes = r.text
soup = bs4(html_bytes, 'lxml')
table = soup.find('table', attrs = {'width': '580'})

rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    columns = [elements.text.strip() for elements in columns]
    data.append([elements for elements in columns if elements])
    
for i in range(len(data)):
    print(data[i][1:4])


# In[ ]:
