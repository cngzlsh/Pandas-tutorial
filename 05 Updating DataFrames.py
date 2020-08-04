people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

import pandas as pd

df = pd.DataFrame(people)
print(df)

# change column
print(df.columns)
df.columns = ['first name', 'last name', 'email_address']
print(df.columns)
# using list complications
df.columns = [x.upper() for x in df.columns]
df.columns = df.columns.str.replace(' ','_')
print(df.columns)
# changing specific cells
df.rename(columns={'FIRST_NAME': 'FIRST', 'LAST_NAME': 'LAST', 'EMAIL_ADDRESS': 'EMAIL'}, inplace=True)
print(df.columns)

# change rows
print(df.loc[2])
df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']
df.at[2, 'EMAIL'] = 'JSmith@email.com'
print(df.loc[2, ['LAST', 'EMAIL']])
# alternatively, use filter
filt = (df['EMAIL'] =='JSmith@email.com')
df.loc[filt, 'LAST'] = 'Smiths'
print(df.loc[2, 'LAST'])
df['EMAIL'] = df['EMAIL'].str.lower()
print(df['EMAIL'])

# using map, apply, function, lambda function etc
print(df['EMAIL'].apply(len))


def update_email(email):
    return email.upper()


print(df['EMAIL'].apply(update_email))
print(df['EMAIL'].apply(lambda x: x.upper()))
# if using (for example) len() on dataframe rather than apply(len), python will return
# the method using series as parameter. eg.
print(len(df['EMAIL']))
print(df.apply(len))
print(df.apply(len, axis ='columns'))
print(df['EMAIL'].apply(len))

print(df.apply(pd.Series.min))
print(df.applymap(str.lower))  # applymap applies to each value in dataframe
print(df.applymap(len))