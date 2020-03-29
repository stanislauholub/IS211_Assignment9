#!/usr/bin/env python
# coding: utf-8

# In[32]:


# PART II: Stock Data

from bs4 import BeautifulSoup
import requests

URL = 'https://www.nasdaq.com/api/v1/historical/AAPL/stocks/2020-02-28/2020-03-28'

data = requests.get(URL).text
data1 = data.split("\n")

for i in range(len(data1) - 1):
    tmp = data1[i].split(",")
    print(tmp[1], "   ", tmp[0])


# In[ ]:
