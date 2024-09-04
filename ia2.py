import pandas as pd
data=pd.read_csv(r"E:\Dataset\auto-mpg.csv")
print(data)
hp_mean=data['Horsepower'].mean
print("mean horsepower\n",hp_mean)
acc_std=data['Acceleration'].std()
print("standard deviation of acceleration\n",acc_std)
manufacture_by_year=data['Model Year'].value_counts().sort_index()
print("no of cars manufacturd in each year\n",manufacture_by_year)
#titanic dataset
import matplotlib.pyplot as plt
data=pd.read_csv(r"E:\Dataset\titanic.csv")
age_survived=data[data['survived']==1]['age']
age_notsurvived=data[data['survived']==0]['age']
plt.hist(age_survived,color='g',alpha=0.9,label='survived')
plt.hist(age_notsurvived,color='k',alpha=0.5,label='notsurvived')
plt.xlabel('age')
plt.ylabel('frequency')
plt.title("age distribution of survived and not survived")
plt.legend()
plt.show()