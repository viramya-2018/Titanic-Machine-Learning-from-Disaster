from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import os

trainFile = pd.read_csv("../data/processed_data/train.csv")
testFile = pd.read_csv("../data/processed_data/test.csv")

trainData = trainFile.values
testData = testFile.values

X = trainData[:,2:]
y = trainData[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=16)
# print (X_train.shape)

model = Sequential()
model.add(Dense(20, input_dim=5, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=120, batch_size=5)

scores = model.evaluate(X_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

y_predict = [1 if value >= 0.5 else 0 for value in model.predict(X_test)]

print ("Accuracy is", accuracy_score(y_test, y_predict))

X_testData = testData[:,1:]
predictLabel_submit = np.array(model.predict(X_testData))
y_predict_submit = [1 if value >= 0.5 else 0 for value in predictLabel_submit]

directory = "../result/"
if not os.path.exists(directory):
    os.makedirs(directory)

res = pd.DataFrame(data=y_predict_submit, columns=['Survived'])
res.to_csv(directory + "submit.csv")