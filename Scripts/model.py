import numpy as np
import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


trainFile = pd.read_csv("../data/processed_data/train.csv")
testFile = pd.read_csv("../data/processed_data/test.csv")

trainData = trainFile.values
testData = testFile.values

X = trainData[:,2:]
y = trainData[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=16)

print len(X_train), len(X_test), len(y_train), len(y_test)

# clf = SVC(C=0.6, kernel='rbf')
# clf = DecisionTreeClassifier(criterion = 'entropy', random_state = 3)
# clf = GaussianNB()

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(20, 4), random_state=1, learning_rate_init=0.01, activation='tanh')
clf.fit(X_train, y_train)

print accuracy_score(y_test, np.array(clf.predict(X_test)))

X_testData = testData[:,1:]
predictLabel_submit = np.array(clf.predict(X_testData))

directory = "../result/"
if not os.path.exists(directory):
    os.makedirs(directory)

res = pd.DataFrame(data=predictLabel_submit, columns=['Survived'])
res.to_csv(directory + "submit.csv")