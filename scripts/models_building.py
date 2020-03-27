# ### Models Building
# 
# Adapting attributes and label to prediction models and performing trainnings. 

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('modified_hotelbookings.csv')
data.head(5)

#separating attributes and labels
label = data.iloc[:, 1].values
attributes_data = data.drop('is_canceled', axis=1)
attributes_data.head(5)

attributes_data.info()

#converting the collumns 0,2,10,11,12,13,17,18,20,22,26
attributes = attributes_data.values

label_encoder = LabelEncoder()
attributes[:, 0] = label_encoder.fit_transform(attributes[:, 0])
attributes[:, 2] = label_encoder.fit_transform(attributes[:, 2])
attributes[:, 10] = label_encoder.fit_transform(attributes[:, 10])
attributes[:, 11] = label_encoder.fit_transform(attributes[:, 11])
attributes[:, 12] = label_encoder.fit_transform(attributes[:, 12])
attributes[:, 13] = label_encoder.fit_transform(attributes[:, 13])
attributes[:, 17] = label_encoder.fit_transform(attributes[:, 17])
attributes[:, 18] = label_encoder.fit_transform(attributes[:, 18])
attributes[:, 20] = label_encoder.fit_transform(attributes[:, 20])
attributes[:, 22] = label_encoder.fit_transform(attributes[:, 22])
attributes[:, 26] = label_encoder.fit_transform(attributes[:, 26])

print('Verifying if there are only numbers in attributes:\n')
print(attributes[0:5])
print('\nAttributes lenght: ', + len(attributes))
print('Labels lenght: ', + len(label))

#importing resources and reports
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

#split train x test
X_train, X_test, y_train, y_test = train_test_split(attributes, label, test_size=0.3, random_state=0)

#function for model training and report
def model_report(model):
    model.fit(X_train, y_train)
    predicts = model.predict(X_test)
    cm = confusion_matrix(y_test, predicts)
    acc = accuracy_score(y_test, predicts)
    cr = classification_report(y_test, predicts)
    print('Confusion Matrix:\n')
    print(cm)
    print('\nAccuracy: ', +  acc*100)
    print('\nClassification Report:')
    print(cr)


# #### Decision Tree Classifier

from sklearn.tree import DecisionTreeClassifier

#training decision tree classifier
dtc = DecisionTreeClassifier()
model_report(dtc)


# #### Logistic Regression

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
model_report(lr)


# #### Naive Bayes (GaussianNB)

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
model_report(nb)