from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectPercentile, f_classif
import numpy as np
from scipy import sparse

def get_initial_trains():
    lines=open('../cleaning data/polarity.txt','r').readlines()[1:]
    number_of_lines=len(lines)
    features_train,labels_train=[],[]
    for i in range(number_of_lines):
        x=lines[i].split(',')
        insult=int(x[0])
        polarity=float(x[1])
        features_train+=[[polarity]]
        labels_train+=[insult]
    return features_train,labels_train

def log_regr_accuracy(features_train,labels_train,features_test,labels_test):
    regr=linear_model.LogisticRegression()
    regr.fit(features_train,labels_train)
    pred=regr.predict(features_test).tolist()
    accuracy=accuracy_score(pred,labels_test)
    return accuracy
def get_data():
    features_train,labels_train=get_initial_trains()
    #features_train=np.array(features_train)
    features_train=sparse.csc_matrix(features_train) 

    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features_train, labels_train, test_size=0.1, random_state=42)
    features_train=features_train.toarray()
    features_test=features_test.toarray()
    return features_train,features_test,labels_train,labels_test
features_train,features_test,labels_train,labels_test=get_data()
print log_regr_accuracy(features_train,labels_train,features_test,labels_test)
