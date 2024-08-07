import data_handler

df, error = data_handler.load_excel('res/Rev Cleanair plot1.csv')
# df, error = data_handler.load_excel('res/Rev Cleanair plot1.xlsx')

# df = df.drop(df.index[-1])
print(df)
# print(df.dtypes)