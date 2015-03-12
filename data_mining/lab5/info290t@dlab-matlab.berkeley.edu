import numpy as np
import pandas as pd
import neurolab as nl # for neural networks
from sklearn import preprocessing, svm
from sklearn.feature_extraction import DictVectorizer #to turn categorial variables into numeric arrays
import datetime as dt

train = pd.read_csv("lab5_train.csv")
train.ZIP_CODE = train.ZIP_CODE.astype("str")
train.TRANSACTION_DT = train.TRANSACTION_DT.astype("int").astype("str")

test = pd.read_csv("lab5_test.csv")
test.ZIP_CODE = train.ZIP_CODE.astype("str")
test.TRANSACTION_DT = train.TRANSACTION_DT.astype("int").astype("str")

le = preprocessing.LabelEncoder()
le.fit(["Obama", "Romney"])
target = le.transform(train.CAND_ID)

# numeric encoding for feature labels
dvec = DictVectorizer()
#only including those features which are not mostly unique values to try and improve the efficiency
feature_cols = [col for col in train.columns if col in ['AMNDT_IND','RPT_TP','ENTITY_TP','CMTE_ID','STATE']]
train_encoding_values = train[feature_cols].T.to_dict().values()
train_encoded_data = dvec.fit_transform(train_encoding_values).toarray()

# Create network with 1 layers
net_4 = nl.net.newff([[0, 1]]*332,[10, 1])
# Train network
error_4 = net_4.train(train_encoded_data, target.reshape(len(target),1), epochs=100, show=100, goal=0.02)
