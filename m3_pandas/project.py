import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')

#def test_preparation(Preparation):
    #test =

#result = df.groupby(by="test preparation course")["math score"].agg([max()])
#print(result)


print(df['test preparation course'].value_counts())
result = df.groupby(by='test preparation course')['math score'].mean()
print(result)

print(df['test preparation course'].value_counts())
result2 = df.groupby(by='test preparation course')['reading score'].mean()
print(result2)

print(df['test preparation course'].value_counts())
result3 = df.groupby(by='test preparation course')['writing score'].mean()
print(result3)


d = df.pivot_table(columns='test preparation course',
                   values='writing score', aggfunc='mean')
d.plot(kind='bar')
plt.show()
