import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data set
df = pd.read_csv("netflix_titles.csv")

# Display the first few rows
print(df.head())
 
# checking for missing values 
missing_value = df.isnull().sum()
print('missing value:/n',missing_value)

# Fill missing values with 'Unknown'
df.fillna("Unknown",inplace=True)

# Task 1: Count of Movies vs Tv Shows
content_type = df['type'].value_counts()
plt.figure(figsize=(4,4))
sns.barplot(x=content_type.index,y=content_type.values)
plt.title("Count of Movie vs . TV Shows on Netflix")
plt.ylabel('Count')
plt.show()

# Task 2: most common genres
df['listed_in'] = df['listed_in'].str.split(",")
all_genres = df.explode('listed_in')
top_genres = all_genres['listed_in'].value_counts().head(10)
print(top_genres)

plt.figure(figsize=(8,4))
sns.barplot(x=top_genres.index,y=top_genres.values,palette="coolwarm")
plt.title("Top 10 Most Genres on Netflix")
plt.xticks(rotation=45)
plt.ylabel('count')
plt.show()

# Task3:Number of Releases per year
df['release_year'] = df['release_year'].astype(int)
yearly_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
sns.lineplot(x = yearly_counts.index, y= yearly_counts.values,marker="o")
plt.title("Number of Movies and TV shows Released Per Year")
plt.xlabel("Year")
plt.ylabel("count")
plt.show()
 
# Task 4: Top 10 Countries Producing Netflix Content
top_countries = df['country'].value_counts().head(10).sort_index()
print(top_countries)

plt.figure(figsize=(8,4))
sns.barplot(x=top_countries.index, y= top_countries.values)
plt.title("Top  10  countries Producing Netflix Content ")
plt.xticks(rotation=45)
plt.ylabel("count")
plt.show()

# Task 5: Relationship Between Duration & Type(Movies vs.TV Shows)
df["duration"] = df["duration"].astype(str).str.extract("(\d+)")  # Extract numbers
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")

plt.figure(figsize=(8, 4))
sns.boxplot(x="type", y="duration", data=df, palette="Set2")
plt.title("Duration Distribution by Content Type (Movies vs. TV Shows)")
plt.ylabel("Duration (Minutes for Movies / Seasons for TV Shows)")
plt.show()
