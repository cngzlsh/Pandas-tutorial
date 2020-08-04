import pandas as pd

# example: dictionary
people = {'first': ['Adam', 'Ben', 'Charlie'],
          'last': ['Daniels', 'Emery', 'Faige'],
          'email': ['adamd@gmail.com', ' bene@gamil.com', 'charlief@gmail.com']}
# extract emails
print(people['email'])

# convert to dataframe
df = pd.DataFrame(people)
print(df)

# access single column
print(df['email'])
print(df.email)  # alternatively
print(type(df['email']))  # series

# access multiple columns
print(df[['last', 'email']])
print(type(df[['last', 'email']]))  # another dataframe

# print all columns
print(df.columns)

# access rows
print(df.iloc[0])
print(df.iloc[[0, 1]])  # rows 0 and 1
print(df.iloc[[0, 1], 2])  # multiple rows but only column 2
print(df.loc[[0, 1], 'email'])  # iloc uses indices while loc uses labels
print(df.loc[[0, 1], ['email', 'last']])

df2 = pd.read_csv('survey_results_public.csv')
print(df2['Hobbyist'])
print(df2['Hobbyist'].value_counts())  # counts data from series
print(df2.loc[0:2, 'Hobbyist':'Employment'])