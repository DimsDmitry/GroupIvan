import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
print(df['Category'].value_counts())

print(100 * '#')
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
ser_cat = df['Content Rating'].value_counts()

result = ser_cat['Teen']/ser_cat['Everyone 10+']
print('Соотношение:', round(result, 2))

# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
result = df.groupby(by='Type')['Rating'].mean()
print(result)

# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
result2 = result['Paid'] - result['Free']
print(round(result2, 2))

# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
table = df.groupby(by='Category')['Size'].agg(['min', 'max'])
print(table)
print(100 * '#')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
result3 = df[df['Rating'] > 4.5]['Category'].value_counts()
print(result3['FINANCE'])
print(100 * '#')

# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
result4 = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(result4['Free']/result4['Paid'])

