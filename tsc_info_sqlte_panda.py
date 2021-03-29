#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import required libraries
import sqlite3
import pandas as pd

# # Read data from the CSV files

tsc_data= pd.read_csv("C:\\Users\\user\\Desktop\\python-files\\teacher_by_status_and_county_for_secondary (1).csv")

print(tsc_data)


# ### Display the first 5 records

# In[3]:


tsc_data.head(5)


# ### Which county as the highest number of teachers?

# In[13]:


tsc_data.groupby('COUNTY').sum()


# ### Clean Up Data

# In[8]:


#check all the NANs
nan_df=tsc_data[tsc_data.isna().any(axis=1)]


# In[ ]:





# In[14]:


import sqlite3, csv

con = sqlite3.connect('tsc1_info.db')
print('db created successcully')


# In[ ]:





# In[ ]:





# In[15]:


import sqlite3, csv

con = sqlite3.connect('tsc5_info.db')
print('db created successcully')


# In[16]:



#create teachers table
c=con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tsc_data2(County_Name text, School_type text, Employment_body text, num_of_teacher int,county text,Year date);")
print('table created successfully')


# In[ ]:


import sqlite3, csv

con = sqlite3.connect('tsc5_info.db')
print('db created successcully')


# In[17]:


#create teachers table
c=con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tsc_data7(County_Name text, School_type text, Employment_body text, num_of_teacher int,Year date);")
print('table created successfully')


# In[18]:


import sqlite3, csv

conn=sqlite3.connect('tsc5_info.db')
c=con.cursor()

with open('C:\\Users\\user\\Desktop\\python-files\\teacher_by_status_and_county_for_secondary1.csv', 'r') as file:
 for row in file:
   c.execute('INSERT INTO tsc_data7 VALUES(?,?,?,?,?)', row.split(','))
print('successful insertion')
rows = c.fetchall()
 
for row in rows:
    print(row)

con.commit()


# In[ ]:




