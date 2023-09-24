import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Шаг 1 - очистка данных
df = pd.read_csv('titanic.csv')
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)


#df.to_csv('titanic_clear.csv')


age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()


def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3
    return row['Age']


df['Age'] = df.apply(fill_age, axis=1)


def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0


df['Sex'] = df['Sex'].apply(fill_sex)

# Шаг 2 - создание модели
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

sc = StandardScaler()
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print('Сравним 5 случайных значений:')
print(y_test[:5])
print(y_pred[:5])

print('Процент правильно предсказанных исходов:', accuracy_score(y_test, y_pred) * 100)
print(confusion_matrix(y_test, y_pred))
