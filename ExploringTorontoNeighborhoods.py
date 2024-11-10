#!/usr/bin/env python
# coding: utf-8

# <center><h1>Exploring Toronto Neighborhoods</h1></center>

# <h3>Data Sources</h3>

# a) Differnt neighborhoods in Toronto are representented by Postal Codes.  I’m using “List of Postal code of Canada: M” (https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M) wiki page to get all the information about the neighborhoods present in Toronto. This page has the postal code, borough & the name of all the neighborhoods present in Toronto.
# 
# b) However, we also need the coordinates of these postal codes to search for compteting businesses.  The “https://cocl.us/Geospatial_data” csv file contains all the geographical coordinates of the neighborhoods.
# We will need to merge the postal code data with the coordinates to create a dataset of all postal code, names of the neighborhood and their respective coordinates.
# 

# ### Part 1
# <h4>Scraping Toronto Neighborhoods Table from Wikipedia “List of Postal code of Canada: M” in order to obtain the data about the Toronto & the Neighborhoods in it.</h4>

# <u> Assumptions made to attain the below DataFrame:</u>
# <li>Dataframe will consist of three columns: PostalCode, Borough, and Neighborhood</li>
# <li>Only the cells that have an assigned borough will be processed. Borough that is not assigned are ignored.</li>
# <li>More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.</li>
# <li>If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.</li>
# 
# wikipedia - package is used to scrape the data from wiki.

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
df = pd.read_html(url)

# the above code captures all the 'tables' found in the webpage and return them in a 'series'
type(df)


# In[4]:


# if you go through the items on the list, you will see the postal code table is the first one in position[0]
df[0]


# In[5]:


# Flatten the DataFrame into one list (a Numpy array)

data = df[0].values.flatten()
data


# In[15]:


# Split the strings in each cell into Postcode, Borough, and Neighbourhood

# hint: use for loop to loop through each item, use string slicing create a list(Postcode, Borough, and Neighbourhood) 
postcode_borough_neigh = []
for item in data:
    # Split on the first space to separate Postcode
    postcode, rest = item.split(' ', 1)
    
    # Check if there's a '(' to separate Borough and Neighbourhood
    if '(' in rest:
        # Split at the first '(' to get Borough and Neighbourhood
        borough, neighbourhood = rest.split('(', 1)
        borough = borough.strip()
        neighbourhood = neighbourhood.strip(')')  # Remove the closing ')'
    else:
        # If no neighbourhood is specified, set it to "Not assigned"
        borough = rest.strip()
        neighbourhood = "Not assigned"
    
    # Append the cleaned data to parsed_data
    postcode_borough_neigh.append([postcode, borough, neighbourhood])

display(postcode_borough_neigh)


# ### if you are doing this correctly, you shall have a list of lists that looks like this:
# ![image.png](attachment:image.png)

# In[16]:


# Create a DataFrame from the cleaned data
columns = ['Postcode', 'Borough', 'Neighbourhood']
df = pd.DataFrame(postcode_borough_neigh, columns=columns)

# Handle multiple neighbourhoods (you can choose to keep them in the same row or split them)
# Assuming you want to handle entries with multiple neighbourhoods by leaving them as comma-separated values:
df['Neighbourhood'] = df['Neighbourhood'].str.replace(' / ', ', ')

# Display the cleaned DataFrame
# Simply use this to display the DataFrame in your local environment
df.head()


# In[17]:


print(df.columns)


# In[18]:


#Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
df = df[df.Borough != 'Not assigned']
df = df.rename(columns={'Postcode': 'Postalcode'})

df


# In[19]:


# Sort data and reset index
df = df.groupby(['Borough', 'Postalcode'])['Neighbourhood'].apply(list).apply(lambda x:', '.join(x)).to_frame().reset_index()
df


# ### Part 2
# <h4>Adding geographical coordinates to the neighborhoods</h4>

# Next important step is adding the geographical coordinates to these neighborhoods. To do so I'm extracting the data present in the Geospatial Data csv file and I'm combining it with the existing neighborhood dataframe by merging them both based on the postal code.  

# In[ ]:


#Reading the latitude & longitude data from CSV file

import io
import requests

url = "https://cocl.us/Geospatial_data"
lat_long = requests.get(url).text
lat_long_df=pd.read_csv(io.StringIO(lat_long))
lat_long_df.head()


# In[ ]:


# renaming the columns to match the existing dataframe  
lat_long_df = lat_long_df.rename(columns={'Postal Code': 'Postalcode'})
lat_long_df.head()


# In[ ]:


# merging both the dataframe into one by matching on the postal code.



# In[ ]:


print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(toronto_DF['Borough'].unique()),
        toronto_DF.shape[0]
    )
)


# ### If you do this right, you shall produce a table like below:
# ![image.png](attachment:image.png)

# ## Very important!
# Save the output as a csv file.
# 
# Upload both this notebook in PDF with output AND the csv file to your GitHub repo.
