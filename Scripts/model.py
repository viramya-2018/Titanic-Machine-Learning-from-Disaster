import numpy as np
import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


trainFile = pd.read_csv("../data/processed_data/train.csv")
testFile = pd.read_csv("../data/processed_data/test.csv")

trainData = trainFile.values
testData = testFile.values

X = trainData[:,2:]
y = trainData[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=16)

print len(X_train), len(X_test), len(y_train), len(y_test)

clf = SVC()
clf.fit(X_train, y_train)


X_testData = testData[:,1:]
print X_testData

predictLabel = np.array(clf.predict(X_testData))

directory = "../result/"
if not os.path.exists(directory):
    os.makedirs(directory)

res = pd.DataFrame(data=predictLabel, columns=['Survived'])
res.to_csv(directory + "submit.csv")