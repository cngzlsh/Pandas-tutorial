people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

import pandas as pd

df = pd.DataFrame(people)

# adding and dropping columns
print(df['first'] + ' ' + df['last'])  # this is a series
df['full_name'] = df['first'] + ' ' + df['last']  # adding a column
print(df)
df.drop(columns=['first', 'last'], inplace=True)
print(df)
print(df['full_name'].str.split(' ', expand=True))  # this outputs two splitted series
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)  # reassign columns
print(df)
df.drop(columns='full_name', inplace=True)

# adding and dropping rows
df.append({'first': 'Tony'}, ignore_index=True)  # use dictionary for append, must state index
people2 = {'email': ['srogers@avengers.com', 'tstark@avengers.com'],
           'first': ['Steve', 'Tony'],
           'last': ['Rogers', 'Starks']}
df2 = pd.DataFrame(people2)
print(df2)
# append can also take a whole dataframe as long as indices options specified
df = df.append(df2, ignore_index=True, sort=False)
print(df)
df.drop(index=df[df['last'] == 'Doe'].index, inplace=True)  # drop takes in a filter by index
print(df)