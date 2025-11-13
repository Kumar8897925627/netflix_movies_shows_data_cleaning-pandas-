import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Downloads\netflix_titles.csv")

# see first 5 rows
print(df.head(1))

# see structure of the dataset
print(df.info())

# renaming column names
df = df.rename(columns=lambda x: x.strip().lower().replace(' ','_'))
print("\ndataframe after renaming columns :")
print(df.columns)

#finding duplicates
duplicates = df.duplicated().sum()
print(duplicates)

# checking null values
print(df.isnull().sum())

#checking and handling nulls in director column
null_count = df['director'].isnull().sum()
print(null_count)
df['director'] = df['director'].fillna('unknown')

has_nulls = df['director'].isnull().any()
print(has_nulls)

# filling missing country names
df['country'] = df['country'].fillna('unknown')

# handling missing cast
df['cast'] = df['cast'].fillna('no cast info')

# fill missing rating
df['rating'] = df['rating'].fillna('not rated')

# changing date format(string to to_date)
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
print(df['date_added'])



