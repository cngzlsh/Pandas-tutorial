import pandas as pd
import numpy as np
people = {
    'first': ['Corey', 'Jane', 'John', 'Adam', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Doe', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com',
              'JohnDoe@gmail.com', 'Adamdoe@gmail.com', None, 'Anonymous@gmail.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']}
df = pd.DataFrame(people)
print(df)

# dropping null data - dropna(axis='index', how='any') as default
print(df.dropna())  # drops NaN, None, etc.
# If how is set to all then it will only drop column/row full of missing values
print(df.dropna(axis='index', how='any', subset=['email']))  # drops all indices where email is null
print(df.dropna(axis='index', how='all', subset=['last', 'email'])) # drops all indices where either email and last is null

# replace all string NA value with np.nan
df.replace('NA', np.nan)
df.replace('Missing', np.nan, inplace=True)
print(df.dropna())
# which are null values?
print(df.isna())
# fill all null values
# print(df.fillna('MISSING'))
print(df.dtypes)

# find mean of age
try:
    print(df['age'].mean())
except TypeError:
    print('TypeError: can only concatenate str (not "int") to str')
    try:
        df['age'] = df['age'].astype(int)
    except TypeError:
        print('TypeError: int() argument must be a string, a bytes-like object or a number, not ''NoneType''')
        df['age'] = df['age'].astype(float)

    print(df['age'].mean())

# real example: stackoverlow survery data
na_vals = ['NA', 'Missing']
df2 = pd.read_csv('survey_results_public.csv', index_col='Respondent', na_values=na_vals)
print(df2['Age'].unique()) # returns an array of unique values
print(df2['Age'].astype(float))
print(df2['Age'].mean())