from logistic_regression import get_data


def DTAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn import tree
    from sklearn.metrics import accuracy_score
    clf = tree.DecisionTreeClassifier(min_samples_split=3,min_samples_leaf=3)
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
    accuracy = accuracy_score(pred,labels_test)
    return accuracy
features_train,features_test,labels_train,labels_test=get_data()

DTAccuracy(features_train,labels_train,features_test,labels_test)
