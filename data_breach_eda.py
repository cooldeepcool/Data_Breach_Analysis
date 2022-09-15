# -*- coding: utf-8 -*-
"""Data Breach EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DQFCxlUWkW4Mi1AUrZl6pndcuw6zy0it

Data Breach Cleaning Exercise - Exploratory Data Analysis
"""

# Commented out IPython magic to ensure Python compatibility.
# Loading the necessary libraries needed for data analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Comment this if the data visualisations doesn't work on your side
# %matplotlib inline

plt.style.use('bmh')

# Loading the file using file upload option

from google.colab import files
 
 
uploaded = files.upload()

# Loading the file with most recent record

import pandas as pd
import io
 
df = pd.read_csv(io.BytesIO(uploaded['DataBreaches.csv']),encoding='windows-1252')
print(df)

#view the data
df.head()

#Basic information

df.info()

#Describe the data

df.describe()

#Find the duplicates

df.duplicated().sum()

#unique values

df['Year'].unique()

df['Method of Leak'].unique()

df['Data Sensitivity'].unique()

#Make a copy:

df_final = df.copy()

print(df_final)

df_final.info()

# Removing double quotes from the string text fields
df_final['Entity'] = df_final['Entity'].apply(lambda x: x.replace('"', ''))

df_final["Alternative Name"] = df["Alternative Name"].astype(str)

df_final['Alternative Name'] = df_final['Alternative Name'].apply(lambda x: x.replace('"', ''))

df_final["Story"] = df["Story"].astype(str)

df_final['Story'] = df_final['Story'].apply(lambda x: x.replace('"', ''))

#Find null values

df.isnull().sum()

#Replace null values
import numpy as np
df_final.replace(np.nan,'0',inplace = True)

#Check the changes now
df_final.isnull().sum()

#Boxplot

df_final[['Number of Records Stolen']].boxplot()

#Correlation plot

sns.heatmap(df_final.corr())

#Converting Data Sensitivity Numeric column into Text details

df_final['Data Sensitivity'] = df_final['Data Sensitivity'].map({1: "Email address/Online Info", 20: "SSN/Personal details", 300: "Credit Card Info", 4000: "Email password/Health records", 50000: "Full bank account details"})

df_final.head()

df_final = df_final.replace(np.nan, '', regex=True)

df_final = df_final.fillna('')

df_final.head()

df_final.to_csv (r'export_dataframe.csv', index = False, header=True)