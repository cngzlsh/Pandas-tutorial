import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
df2 = pd.read_csv('survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_column', 60)
print(df.head(5))

# aggregation: combining multiple data into a single result
print(df['ConvertedComp'].median())
print(df.median())
print(df.describe())
print(df['Trans'].value_counts())

# grouping: spliting, applying function, combine results
print(df['Country'])
country_group = df.groupby(['Country'])  # group by countries
print(country_group.get_group('Botswana'))
print(country_group['ConvertedComp'].value_counts())
print(country_group['ConvertedComp'].value_counts(normalize=True).loc['China'])
print(country_group['ConvertedComp'].median().loc['Germany'])

print(country_group['ConvertedComp'].agg(['median', 'mean']).loc['Canada'])
