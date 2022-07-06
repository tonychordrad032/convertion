import pandas as pd

# read pdf file and assign it to df
df = pd.read_csv("AlternativeMethod.csv", on_bad_lines='skip')

# in the first column all values with NaN will be filled with 0
df['Unnamed: 0'] = df['Unnamed: 0'].fillna(0)

# The condition to select data where first column == 0
filt = df['Unnamed: 0'] == 0

# parsing the condition named filt in the reversed form by using ~ and we specify The range of columns we need
df2 = df.loc[~filt, 'Unnamed: 0': 'Unnamed: 10']

# save to csv file
df2.to_csv('final.csv', index=False)
