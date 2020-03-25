# reference - https://www.geeksforgeeks.org/multiclass-classification-using-scikit-learn/

def DecisionTreeClassifier_Model(X_train,y_train,X_test):
    from sklearn.tree import DecisionTreeClassifier
    dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
    y_predict = dtree_model.predict(X_test)
    return y_predict

def SVC_Model(X_train,y_train,X_test):
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
    y_predict = svm_model_linear.predict(X_test)
    return y_predict

# KNN (k-nearest neighbours) classifier
def KNeighborsClassifier_Model(X_train,y_train,X_test) :
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
    y_predict = knn.predict(X_test)
    return y_predict

# Naive Bayes classifier
def GaussianNB_model(X_train,y_train,X_test) :
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB().fit(X_train, y_train)
    y_predict = gnb.predict(X_test)
    return y_predict

# reference - https://medium.com/@b.terryjack/tips-and-tricks-for-multi-class-classification-c184ae1c8ffc
def RandomForestClassifier_model(X_train,y_train,X_test) :
    from sklearn.ensemble import RandomForestClassifier
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)
    y_predict = rf_classifier.predict(X_test)
    return y_predict

def MLPClassifier_model(X_train,y_train,X_test):
    from sklearn.neural_network import MLPClassifier
    snn_classifier = MLPClassifier()
    snn_classifier.fit(X_train, y_train)
    y_predict = snn_classifier.predict(X_test)
    return y_predict