import pandas as pd 


df = pd.read_csv("raw_files/population.csv")
# df = df[ df["Country Name"] == "Nigeria" ] 

# Dropping unnecessary columns
df = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 67'])

# set Country Name as index and transpose
df = df.set_index('Country Name').T

# return country name as column by dropping index and renaming the column
df.reset_index(drop=False, inplace=True)
df.rename(columns = {'index':'Year'}, inplace = True) 

df.to_csv('processed_files/population.csv', index=False)