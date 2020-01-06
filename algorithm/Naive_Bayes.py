# Scikit-learn docs https://scikit-learn.org/stable/modules/naive_bayes.html

from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics

org_data = []
org_label = []
X_train = [], X_test = [], Y_train = [], Y_test = []

clf_1 = Pipeline([('vect', CountVectorizer()), ('clf', MultinomialNB(alpha=1.0))])
clf_2 = Pipeline([('vect', TfidfVectorizer()), ('clf', MultinomialNB(alpha=1.0))])
clf_3 = Pipeline([('vect', CountVectorizer()), ('clf', GaussianNB())])

def train_and_evaluate(clf, X_train, X_test, Y_train, Y_test):
    clf.fit(X_train, Y_train)
    print("Accuracy on Training set: ")
    print(clf.score(X_train, Y_train))
    print("Accuracy on Testing set: ")
    print(clf.score(X_test, Y_test))
    y_pred = clf.predict(X_test)

    print("Classification Report: ")
    print(metrics.classification_report(Y_test, y_pred))
    print(metrics.confusion_matrix(Y_test, y_pred))

def split():
    SPLIT_PERC = 0.75
    split_size = int(len(org_data)*SPLIT_PERC)
    X_train = org_data[:split_size]
    X_test = org_data[split_size:]
    Y_train = org_label[:split_size]
    Y_test = org_label[split_size:]

# Multi-class
train_and_evaluate(clf_1, X_train, X_test, Y_train, Y_test)