# ### Data Wrangling
# 
# Performing transformations in data to adapt to prediction models.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import data
data = pd.read_csv('hotel_bookings.csv')


# Checking for the existence of null values in each variable.
def num_missing(x):
    return sum(x.isnull())

#applying in collumns
print('Number of missing values by collumns:')
print(data.apply(num_missing, axis = 0))


# The "agent" and "company" variables have many null values and do not seem to be significant for the model, so I performed the removal.
data = data.drop(['agent', 'company'], axis=1)


# Analyzing the lead time variable distribution earlier, I noticed an asymmetric distribution. I decided to check for outliers and perform a logarithmic normalization process.

#checking outliers in lead_time variable
sns.boxplot(data['hotel'], data['lead_time'], orient="v")

#log transformation
leadtime = data.iloc[:, 2]
leadtime_zero = []
for value in leadtime:
    if value == 0:
        leadtime_zero.append(leadtime)

print('Zero values: ', + len(leadtime_zero))

leadtime_log = []
for value in leadtime:
    if value == 0:
        leadtime_log.append(np.log(value+1))
    else:
        leadtime_log.append(np.log(value))
        
#checking if persists the same samples size
print(len(leadtime_log))

#converting in numpy array
leadtime_log = np.asarray(leadtime_log)
print(leadtime_log)

data['lead_time_log'] = leadtime_log
data.head(10)

#comparing lead_time before and after log normalization
plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
data['lead_time'].hist()
plt.title('lead_time original')

plt.subplot(2,2,2)
data['lead_time_log'].hist()
plt.title('lead_time with log')

#checking if the outliers still persists.
sns.boxplot(data['hotel'], data['lead_time_log'], orient="v")

# Replacing missing values in children variable by the mean and country variable by the mode.
data['children'].fillna(data['children'].mean(), inplace=True)
data['country'].fillna(data['country'].mode()[0], inplace=True)

#verifying missing values
print(data.apply(num_missing, axis = 0))

#removing lead_time and reservation_status_date
data = data.drop(['lead_time', 'reservation_status_date'], axis=1)
data.head(10)

#saving new data
data.to_csv(r'.\modified_hotelbookings.csv', index=False, header=True)