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
education_mask = df.headline_text.str.contains("education", case=True,
                                     na=None, regex=False)
# print(f"{df[education_mask].shape[0]} headlines found!") # 9299 headlines
# print(f"{df[education_mask].head(9299)}") # printing all the 9299 headlines found



# counting the occurrences of the word "employment" across the dataset
employment_mask = df.headline_text.str.contains("employment", case=True,
                                           na=None, regex=False)
# print(f"{df[employment_mask].shape[0]} headlines found!") # 1008 headlines found
# print(f"{df[employment_mask].head()}") # printing all the 1008 headlines found