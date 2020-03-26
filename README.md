## Kaggle Hotel Booking Task

This is a repository of my kernel for Hotel Booking task in Kaggle. The objective was predict the cancellation of booking based on many features.

The features descriptions are presents in [collumns_descriptions.txt](https://github.com/LeAmSa/Kaggle-Hotel-Booking/blob/master/collumns_descriptions.txt "collumns_descriptions.txt")

The Kernel contains Exploratory Data Analysis, Data Wrangling and Predict Models Building.

All steps above are split in jupyter notebooks: 

 - __EDA__: [data_exploration.ipynb](https://github.com/LeAmSa/Kaggle-Hotel-Booking/blob/master/data_exploration.ipynb "data_exploration.ipynb").
- __Data Wrangling__: [data_wrangling.ipynb](https://github.com/LeAmSa/Kaggle-Hotel-Booking/blob/master/data_wrangling.ipynb "data_wrangling.ipynb").
- __Predict Models Building__: [models_building.ipynb](https://github.com/LeAmSa/Kaggle-Hotel-Booking/blob/master/models_building.ipynb "models_building.ipynb").

The main notebook with sequential steps are in [EDA, Data Wrangling and Models for Hotel Booking.ipynb](https://github.com/LeAmSa/Kaggle-Hotel-Booking/blob/master/EDA%2C%20Data%20Wrangling%20and%20Models%20for%20Hotel%20Booking.ipynb "EDA, Data Wrangling and Models for Hotel Booking.ipynb").

### Prediction Models and results
I chose work with three machine learning models: __Decision Tree Classifier__, __Gaussian Naive Bayes__ and __Logistic Regression__.

The table bellow presents my classification results:
| Algorithm | Accuracy |
|--|--|
| DecisionTreeClassifier | 100%(overfitting) |
| GaussianNB | 99.23% |
| LogisticRegression | 98.92% |







