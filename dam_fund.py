#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.scp.gov.pk/DonationChart.aspx"

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

rows = soup.find_all('tr')

for row in rows:
    row_td = row.find_all('td')

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()

numstring = ""
for x in range(20,34):
    numstring+=cleantext[x]

s = ''.join(x for x in numstring if x.isdigit())
amount_collected = int(s)
print(amount_collected)
