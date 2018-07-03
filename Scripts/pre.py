import numpy as np
import pandas as pd

data = pd.read_csv("../data/train.csv")
data = pd.DataFrame(data)

# 
mappingSex = {'male': 1, 'female': 0}
data = data.replace({'Sex': mappingSex})

mappingEmbarked = {'S': 0, 'C': 1, 'Q': 2}
data = data.replace({'Embarked': mappingEmbarked})

# dataTrain = data.loc[:, ['Survived', 'Pclass', 'Sex', 'Age']]
