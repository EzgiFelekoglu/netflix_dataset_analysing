#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing dataset
import pandas as pd
mydata=pd.read_csv(r'netflix_titles.csv')


# # 1. head()
# 

# In[2]:


# showing top 5 records


# In[3]:


mydata.head()


# # 2. tail()

# In[4]:


# showing bottom 5 records


# In[5]:


mydata.tail()


# # 3. shape, columns

# In[6]:


# showing the number of rows and columns
mydata.shape


# In[7]:


# showing each column name
mydata.columns


#  # 4. dtypes and info()

# In[8]:


# showing data-type for each column
mydata.dtypes


# In[9]:


# showing indexes,columns,data-types of each column
mydata.info()


# # Task 1- Removing the duplicate records

# # duplicate()

# In[10]:


mydata[mydata.duplicated()]


# # Task 2-Null Values 

# In[11]:


mydata.isnull()


# In[12]:


# showing count of Null values for each column
mydata.isnull().sum()


# In[13]:


import seaborn as sns 


# In[14]:


#using heat-mat to show null values count
sns.heatmap(mydata.isnull())


# # Task 3

# # -  isin()

# In[15]:


### Question-- What is the 'release year' and 'rating' for 'Zombie Dumb' and 'Jaguar' ?


# In[16]:


mydata[mydata['title'].isin(['Zombie Dumb','Jaguar'])]


# # Task 4 

# In[17]:


### Question-- In which year highest number of the TV Shows & Movies were released? Show with Bar Graph.


# In[18]:


mydata.dtypes


# In[19]:


## to_datetime (Convert argument to datetime and create new column.)


# In[20]:


mydata['Date_converted']=pd.to_datetime(mydata['date_added'])


# In[21]:


mydata.head()


# In[22]:


# counting all individual years in Date_converted column.
mydata['Date_converted'].dt.year.value_counts()


# In[23]:


mydata['Date_converted'].dt.year.value_counts().plot(kind='bar')


# # Task 5

# In[24]:


### Question--How many Movies&TV Shows are in the dataset?


# # groupby()

# In[25]:


mydata.groupby('type').type.count()


# In[26]:


sns.countplot(mydata['type'])


# # Task 6

# In[27]:


### Question-- All the TV Shows that were released in 2019?


# In[28]:


##Creating new column 'Date_Converted_Year'
mydata['Date_Converted_Year']=mydata['Date_converted'].dt.year


# In[29]:


mydata.head(1)


# In[30]:


####### FILTERING ######


# In[31]:


mydata[(mydata['type']=='TV Show')&(mydata['Date_Converted_Year']==2019)].head()


# In[32]:


# Show directors of all Movies that were released in South Korea only.


# In[33]:


mydata[(mydata['type']=='Movie')&(mydata['country']=='South Korea')] ['director']


# In[34]:


### Find Directors who gave the highest number of TV Show and Movies to Netflix? 


# In[35]:


mydata['director'].value_counts().head()


# In[36]:


## Show all TV Shows that listed_in 'Docuseries'
mydata[(mydata['type']=='TV Show')&(mydata['listed_in']=='Docuseries')]


# # Creating new data-frame 

# In[37]:


## Drop the rows that contains missing values.


# In[38]:


mydata_new=mydata.dropna()


# In[39]:


mydata_new.head()


# In[40]:


# Finding 'Morgan Freeman' in column named 'cast'
mydata_new[mydata_new['cast'].str.contains('Morgan Freeman')]


# # nunique() , unique()

# In[41]:


## different ratings defined by Netflix


# In[42]:


mydata['rating'].nunique()


# In[43]:


mydata['rating'].unique()


# In[44]:


### Question-- How many movies got the 'NC-17' rating ?


# In[53]:


mydata[(mydata['type']=='Movie') & (mydata['rating']=='TV-G') & (mydata['country']=='Germany')]


# In[56]:


mydata[(mydata['type']=='Movie') & (mydata['rating']=='TV-G') & (mydata['country']=='Germany')
       & (mydata['Date_Converted_Year']<2020)]


# In[57]:


## Question-- Maximum duration of a Movie/Show on Netflix ?


# In[61]:


mydata['duration'].unique()


# In[62]:


mydata.duration.dtypes


# # str.split()

# In[63]:


## splitting 'duration'


# In[66]:


mydata[['Minutes','Unit']] = mydata['duration'].str.split(' ',expand=True)


# In[67]:


mydata.head(3)


# In[68]:


### Which Individual country has the Highest number of Movies?


# In[69]:


mydata_movies=mydata[mydata['type']=='Movie']


# In[70]:


mydata_movies.head(2)


# In[73]:


mydata_movies.country.value_counts()


# In[81]:


### Sorting the dataset by the year ?


# In[83]:


mydata.sort_values(by='Date_Converted_Year',ascending=False)


# In[84]:


### Type is 'Movie' and 'listed_in' 'Family Movies' or
### Type is 'TV show' and 'listed_in' 'International TV Shows'


# In[85]:


mydata.head()


# In[94]:


mydata[(mydata['type']=='Movie') & (mydata['listed_in'].str.contains('Family Movies'))]


# In[97]:


mydata[(mydata['type']=='TV Show') & (mydata['listed_in'].str.contains('Romantic TV Shows'))]


# In[98]:


mydata[(mydata['type']=='Movie') & (mydata['listed_in'].str.contains('Family Movies')) | (mydata['type']=='TV Show') & (mydata['listed_in'].str.contains('Romantic TV Shows'))]


# In[ ]:




