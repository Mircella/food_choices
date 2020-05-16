#data preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import the data
food_coded_original = pd.read_csv('food_coded.csv')
food_coded = food_coded_original.copy()

#---clean GPA to have only floats
#food_coded['GPA'] = food_coded['GPA'].str.replace(r'\D+','') - leave only digits
food_coded['GPA'] = food_coded['GPA'].str.replace(r'[a-zA-Z]','')
food_coded['GPA'] = food_coded['GPA'].replace(['', ' '], np.NaN)
food_coded = food_coded[food_coded['GPA'].notna()]
food_coded['GPA'] = food_coded['GPA'].astype(float)

#The barplot for gender
gender = food_coded[['Gender', 'GPA']]
gpa = gender.groupby('Gender').mean()
subjects = ['Female', 'Male']
indx = np.arange(len(subjects))
bar_width = 0.50

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{0:.3f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


fig, ax = plt.subplots(figsize = (10,7))
female_rect = plt.bar(0, gpa.iloc[0],bar_width, label = 'Female')
male_rect = plt.bar(1, gpa.iloc[1],bar_width, label = 'Male')
ax.set_ylabel('GPA', fontsize = 14)
ax.set_title('Female and Male GPA', fontsize = 16)
ax.set_xticks(indx)
ax.set_xticklabels(subjects, fontsize = 14)
ax.legend(fontsize = 12, loc = (1.01, 0.4))
autolabel(female_rect)
autolabel(male_rect)
plt.show()


#Current Diet Pie Chart
diet = food_coded.groupby('diet_current_coded')['Gender'].count().reset_index()
labels = ['healthy', 'unhealthy', 'constant food', 'unclear']
fig1, ax1 = plt.subplots(figsize = (10,7))
plt.title("Strudents' Diet", fontsize = 16)
explode = (0.1,0.1,0,0)
ax1.pie(diet.iloc[:,1],explode = explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()


#Gender Diet GPA
gender_diet_gpa = food_coded.groupby(['Gender', 'diet_current_coded'])['GPA'].mean().reset_index().T
labels = ['Female','Male']
indx = np.arange(len(labels))
bar_width = 0.25
fig, ax = plt.subplots(figsize = (16,7))
healthy = plt.bar(indx+0.00, gender_diet_gpa.iloc[2,[0,4]],bar_width, label = 'healthy')
unhealthy = plt.bar(indx+0.22, gender_diet_gpa.iloc[2,[1,5]],bar_width, label = 'unhealthy')
const = plt.bar(indx+0.44, gender_diet_gpa.iloc[2,[2,6]],bar_width, label = 'constant food')
unclear = plt.bar(indx+0.66, gender_diet_gpa.iloc[2,[3,7]],bar_width, label = 'unclear')
ax.set_ylabel('GPA', fontsize = 14)
ax.set_title('Average GPA Grouped by Diet Type', fontsize = 16)
plt.xticks(indx,labels, fontsize = 20)

#ax.set_xticks(indx)
#ax.set_xticklabels(labels, fontsize = 15)
ax.legend(fontsize = 12, loc = (1.01, 0.4))
autolabel(healthy)
autolabel(unhealthy)
autolabel(const)
autolabel(unclear)
plt.show()





