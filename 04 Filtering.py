# Using conditionals to filter rows and columns
people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

import pandas as pd

df = pd.DataFrame(people)

print(df)

# compare Does and create filter
print(df['last'] == 'Doe')
filt = (df['last'] == 'Doe')

# apply filter
print(df[filt])
print(df.loc[filt], 'email')

# 'and' and 'or': & and |
filt = (df['last'] == 'Schafer') | (df['first'] == 'John')
print(df[filt])
print(df.loc[-filt, 'email'])

df2 = pd.read_csv('survey_results_public.csv', index_col='Respondent')
df3 = pd.read_csv('survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_rows', 61)
print(df3)

ea = df2['Ethnicity'] == 'East Asian'
# high_exp = (int(df2['YearsCode']) > 5)
print(df2.loc[ea, 'Country'])
countries = ['United States', 'United Kingdom', 'Germany', 'France', 'Canada', 'Australia']
countries_filt = df2['Country'].isin(countries)
print(df2.loc[countries_filt, 'Ethnicity'])

ethnicity_filt = df2['Ethnicity'].str.contains('White', na=False)
print(df2.loc[ethnicity_filt, 'Country'])