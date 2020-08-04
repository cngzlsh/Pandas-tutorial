import pandas as pd

people = {'first': ['Adam', 'Ben', 'Charlie'],
          'last': ['Daniels', 'Emery', 'Faige'],
          'email': ['adamd@gmail.com', 'bene@gmail.com', 'charlief@gmail.com']}

# pd.DataFrame converts a dictionary into a dataframe
df = pd.DataFrame(people)
print(df)

print(df['email'])
# set email address as the index of all columns, this wont change original dataframe
# unless parameter inplace is set to true
df.set_index('email', inplace=True)
print(df)

print(df.loc['bene@gmail.com', 'last'])

# reset index
df.reset_index(inplace=True)
print(df)

df2 = pd.read_csv('survey_results_public.csv', index_col='Respondent')
df3 = pd.read_csv('survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 61)
pd.set_option('display.max_rows', 61)
print(df2.head())
print(df3)
print(df3.loc['NEWLearn'])

print(df3.sort_index(ascending=False))