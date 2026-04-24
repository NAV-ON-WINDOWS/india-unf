import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# keeping track of years when "education" was mentioned
"""
using boolean indexing
"""
ed_mask = df['headline_text'].str.contains("education", case=False, na=False)
ed_df = df[ed_mask]
ed_df = ed_df.copy() # gives a new dataframe
ed_df['year'] = ed_df.publish_date.astype(str).str[:4]
ed_by_year = ed_df['year'].value_counts().sort_index()
# print(ed_by_year)


# counting the occurrences of the word "employment" across the dataset
employment_mask = df.headline_text.str.contains("employment", case=True,
                                           na=None, regex=False)
# print(f"{df[employment_mask].shape[0]} headlines found!") # 1008 headlines found
# print(f"{df[employment_mask].head()}") # printing all the 1008 headlines found

# keeping track of years when "employment" was mentioned
"""
using boolean indexing
"""
emp_mask = df['headline_text'].str.contains('employment', case=False, na=False)
emp_df = df[emp_mask]
emp_df = emp_df.copy() # gives a new dataframe
emp_df['year'] = emp_df['publish_date'].astype(str).str[:4]
emp_df_year = emp_df['year'].value_counts().sort_index()
# print(emp_df_year)


# combine both the dataframes
df_combined = pd.concat([ed_df, emp_df], ignore_index=True)
# print(df_combined)


# combined years
years = ed_by_year.index.union(emp_df_year.index)


# matplotlib plotting
fig, ax = plt.subplots(figsize=(13.66, 7.68))
manager = plt.get_current_fig_manager()
manager.full_screen_toggle() # manager sets res to fullscreen

# adding title and subtitle
ax.set_title("Headline frequency analysis across Indian news (2001–2023)",
             fontsize=9, color='gray', pad=25)
fig.suptitle("Education v/s Employment", fontsize=14, fontweight='bold')

# axis labelling
ax.plot(ed_by_year.index, ed_by_year.values, label="Education", marker='o')
ax.plot(emp_df_year.index, emp_df_year.values, label="Employment", marker='o')
ax.legend(loc="upper right", frameon=True)

# adding grid
ax.grid(True, linestyle='-', which='major')
ax.tick_params(axis='both')

ax.yaxis.set_major_locator(plt.MultipleLocator(100)) # y grid lines every 100 px
ax.xaxis.set_major_locator(plt.MultipleLocator(1)) # x grid lines year

# adding peak annotations
peak_ed_year = ed_by_year.idxmax()
peak_ed_val = ed_by_year.max()
ax.annotate(f"Peak = {peak_ed_val}",
            xy=(peak_ed_year, peak_ed_val),
            xytext=(0, 10),              # Move 10 points straight up from the point
            textcoords="offset points",   # Interpret (0, 10) as an offset, not a year/value
            ha='center',                  # Centers the text horizontally over the point
            arrowprops=dict(arrowstyle="->"))

peak_emp_year = emp_df_year.idxmax()
peak_emp_value = emp_df_year.max()
ax.annotate(f"Peak = {peak_emp_value}",
            xy=(peak_emp_year, peak_emp_value),
            xytext=(0, 50),              # Increased offset to clear the lines
            textcoords="offset points",
            ha='center',
            arrowprops=dict(arrowstyle="->"))


ax.set_ylim(bottom=0)
ax.set_xlim(left=0)

plt.show()