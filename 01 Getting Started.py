import pandas as pd

# loading csv data
df = pd.read_csv('survey_results_public.csv')
print(df.shape)
print(df.info())

pd.set_option('display.max_columns', 61)
print(df)  # now shows 85 entries

pd.set_option('display.max_rows', 85)
schema_df = pd.read_csv('survey_results_schema.csv')
print(schema_df)
print(schema_df.head())  # show first 5
print(schema_df.tail(5))  # show last 5

