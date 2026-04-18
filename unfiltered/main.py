import pandas as pd

# creating dataset and setting it to display max columns
dataset = "india-news-headlines.csv"
df = pd.read_csv(dataset)
pd.set_option('display.max_columns', None)
# print(df)