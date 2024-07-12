import pandas as pd

swift_df = pd.read_csv(
    'C:/Users/KateJoyce/Desktop/Python/Preppin_Data/Swift Codes.csv')
trans_df = pd.read_csv(
    'C:/Users/KateJoyce/Desktop/Python/Preppin_Data/Transactions.csv')

print(trans_df)
# In the Transactions table, there is a Sort Code field which contains dashes.
# We need to remove these so just have a 6 digit string
trans_df['Sort Code'] = trans_df['Sort Code'].str.replace(
    '-', '', regex=False)
print(trans_df)

# Use the SWIFT Bank Code lookup table to bring in additional information
# about the SWIFT code and Check Digits of the receiving bank account
df = trans_df.merge(swift_df, how='inner', on='Bank')

print(df)

# Add a field for the Country Code
df['Country Code'] = 'GB'


# Create the IBAN as above
# Hint: watch out for trying to combine sting fields with numeric fields - check data types
df['IBAN'] = df['Country Code'] + df['Check Digits'] + \
    df['SWIFT code'] + df['Sort Code'] + df['Account Number'].astype(str)

print(df)
# Remove unnecessary fields
output_df = df[['Transaction ID', 'IBAN']]

print(output_df)

# Output the data
output_df.to_csv(
    'C:/Users/KateJoyce/Desktop/Python/Preppin_Data/pd2023wk02_output.csv', index=False)
