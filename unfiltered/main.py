import pandas as pd

# creating dataset and setting it to display max columns
dataset = "india-news-headlines.csv"
df = pd.read_csv(dataset)
pd.set_option('display.max_columns', None)
# print(df)

# checking for null values
n_null = df.isnull()
# print(n_null.sum()) # there are no null values in the dataset

"""
since there are no null values,
we don't need to fill none values,
or,
replace the duplicates,
"""

# counting the occurrences of the word "education" across the dataset
education = df.headline_text.str.contains("education", case=True,
                                     na=None, regex=False)
print(f"{df[education].shape[0]} headlines found!") # 9299 headlines
print(f"{df[education].head(9299)}") # printing all the 9299 headlines found