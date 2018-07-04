import numpy as np
import pandas as pd
import math
import sys
import os
from matplotlib import pyplot as plt

fileName = sys.argv[1]
fileName = fileName + ".csv"
data = pd.read_csv("../data/" + fileName)
data = pd.DataFrame(data)

# print data.describe()

# mapping male to 1 and female to 0
mappingSex = {'male': 1, 'female': 0}
data = data.replace({'Sex': mappingSex})

# mapping S to 0, C to 1 and Q to 2
mappingEmbarked = {'S': 0, 'C': 1, 'Q': 2}
data = data.replace({'Embarked': mappingEmbarked})

# calculating the mean male and female ages
meanAge_female = data['Age'].groupby(data['Sex']).describe()[0]['mean']
meanAge_male = data['Age'].groupby(data['Sex']).describe()[1]['mean']

# replacing NaN with mean ages of males and females respectively
arr = data.values
# print arr
# print data.describe()
if(sys.argv[1] == 'train'):
    for i in arr:
        if i[4] == 0 and not (i[5] == i[5]):
            i[5] = meanAge_female
        elif i[4] == 1 and not (i[5] == i[5]):
            i[5] = meanAge_male
if(sys.argv[1] == 'test'):
    for i in arr:
        if i[3] == 0 and not (i[4] == i[4]):
            i[4] = meanAge_female
        elif i[3] == 1 and not (i[4] == i[4]):
            i[4] = meanAge_male

data.iloc[:,:] = arr

# replacing NaN with 0 for embarked as it the most common source
data['Embarked'] = data['Embarked'].fillna(value=0.0)

if(sys.argv[1] == 'train'):
    data = data.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
if(sys.argv[1] == 'test'):
    data = data.loc[:, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]

directory = "../data/processed_data/"

if not os.path.exists(directory):
    os.makedirs(directory)

data.to_csv(directory + fileName)

print "Length of the " + fileName + " is " + str(len(data))