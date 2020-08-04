people = {
    'first': ['Corey', 'Jane', 'John','Adam'],
    'last': ['Schafer', 'Doe', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com',
              'JohnDoe@gmail.com', 'Adamdoe@gmail.com']}

import pandas as pd

df = pd.DataFrame(people)
print(df)

# sort by column
print(df.sort_values(by='last'))
print(df.sort_values(by='last', ascending=False))  # ascending order
print(df.sort_values(by=['last', 'first']))  # sorting by multiple columns
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)
print(df)

df2 = pd.read_csv('survey_results_public.csv', index_col='Respondent')
df3 = pd.read_csv('survey_results_schema.csv', index_col='Column')

print(df3)

# sort by country
df2.sort_values(by=['Country', 'Age'], ascending=[True, False], inplace=True)
print(df2[['Country', 'Age']].head(20))
print(df2['Age'].nlargest(10))  # print 10 oldest respondents
print(df2.nsmallest(10, 'Age'))