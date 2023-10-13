import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('train.csv')
print(df.info())

# удаляем лишние столбцы
df = df.drop(['life_main', 'city', 'people_main', 'last_seen', 'occupation_name'], axis=1)
df.dropna(inplace=True)
print(df.info())


# замена текстовых данных
# форма образования. Part-time - 0
# Distance Learning - 1
# Full-time - 2
def change_edu(row):
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row


df.apply(change_edu, axis=1)


# заменим значения даты рождения на возраст.
# берём год рождения, вычитаем его из 2023.
# 11.5.1991 -> 1991
def change_bdata(row):
    bdate = row['bdate'].split('.')
    if len(bdate) == 3:
        row['bdate'] = 2023 - int(bdate[2])
    else:
        row['bdate'] = np.nan
    return row


df.apply(change_bdata, axis=1)


# статус образования
def change_edu(row):
    row = row.replace('Student (Specialist)', 0)
    row = row.replace('Alumnus (Specialist)', 1)
    row = row.replace('PhD', 2)
    row = row.replace("Student (Bachelor's)", 3)
    row = row.replace("Alumnus (Master's)", 4)
    row = row.replace("Alumnus (Bachelor's)", 5)
    row = row.replace("Student (Master's)", 6)
    row = row.replace('Undergraduate applicant', 7)
    row = row.replace('Candidate of Sciences', 8)
    return row


df.apply(change_edu, axis=1)

print('=' * 10)
print(df['langs'].value_counts())
print('#' * 10)
print(df['occupation_type'].value_counts())
print('#' * 10)
print(df['career_start'].value_counts())
print('#' * 10)
print(df['career_end'].value_counts())
print('#' * 10)


# выясним кол-во языков, которые знает человек
def change_langs(row):
    try:
        langs = row['langs']
        langs = langs.split(';')
        n_langs = len(langs)
    except:
        n_langs = 0
    return n_langs
