#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pandas.io.json import json_normalize

#Connect to service account
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('', scope)

gc=gspread.authorize(credentials)

#Get candidate data sheet from Google Drive
spreadsheet_key = '' 
#Delete spreadsheet key before uploading

book = gc.open_by_key(spreadsheet_key) 
worksheet = book.worksheet("Reorganized GBW Data") 
table = worksheet.get_all_values()
print(table)

table[0][1]

##Convert table data into a dataframe
df = pd.DataFrame(table[1:], columns=table[0])
# table[1:] means start at first element (not 0th element) and keep going
df






# In[5]:


df.iloc(0)


# In[ ]:




