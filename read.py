import pandas as pd

excel_file = 'books.xlsx'

df = pd.read_excel(excel_file,  usecols=['authors'])

print(df)

#new_dict = df.to_dict()
#print(new_dict)

