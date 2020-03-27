import pandas as pd

#import data
data = pd.read_csv('hotel_bookings.csv')
data.head(10)

# ### Analyzing the raw data (EDA)
# 
# Exploring the types of each variable and some basic statistical information.
data.info()

#only the categorical ones
data.describe(include='object').T

#only int and float
data.describe(exclude='object').T


# ### Graphical Analysis
# 
# Analyzing the behavior of some variables and checking the need for normalization of quantitative variables.

import seaborn as sns
import matplotlib.pyplot as plt

#checking the hotel types distribution
sns.countplot(data['hotel'], palette='pastel')

#checking the proportion of canceled bookings
plot = sns.countplot(data['is_canceled'], palette='pastel')
plot.set_xlabel("Canceled")

#checking previous cancellations by hotel type on years
plt.figure(figsize=(15,10))
plot = sns.barplot(data['arrival_date_year'], data['previous_cancellations'], hue=data['hotel'], palette='pastel')
plot.set_xlabel("Arrival Year")
plot.set_ylabel("Previous Cancellations")

#checking previous cancellations on arrival months on each year
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']

plt.figure(figsize=(15,10))
plot = sns.barplot(data['arrival_date_month'], data['previous_cancellations'], hue=data['arrival_date_year'], order=month_order)
plot.set_xlabel("Arrival Month", fontsize=15)
plot.set_ylabel("Previous Cancellations", fontsize=15)
plt.legend(loc='best')

#checking the frequency of the segments for which reservations were made
plt.figure(figsize=(15,10))
sns.countplot(data['market_segment'], palette='pastel')

#checking the years distribution
sns.countplot(data['arrival_date_year'], palette='pastel')

#Checking the months distribution
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']

plt.figure(figsize=(15,10))
sns.countplot(data['arrival_date_month'], order=month_order, palette='pastel')


# ### Checking distribution of some variables

#fig1
f = plt.figure(figsize=(6,6))
grid_spec = f.add_gridspec(2,2)

ax = f.add_subplot(grid_spec[0,0])
sns.distplot(data['lead_time'], kde=False)

ax = f.add_subplot(grid_spec[0,1])
sns.distplot(data['stays_in_weekend_nights'], bins=20, kde=False)

ax = f.add_subplot(grid_spec[1,0])
sns.distplot(data['stays_in_week_nights'], kde=False)

ax = f.add_subplot(grid_spec[1,1])
sns.distplot(data['previous_cancellations'], kde=False)

f.tight_layout()

#fig2

f = plt.figure(figsize=(9,3))
grid_spec = f.add_gridspec(1,3)

ax = f.add_subplot(grid_spec[0,0])
sns.distplot(data['adr'], kde=False)

ax = f.add_subplot(grid_spec[0,1])
sns.distplot(data['required_car_parking_spaces'], kde=False)

ax = f.add_subplot(grid_spec[0,-1])
sns.distplot(data['total_of_special_requests'], kde=False)


f.tight_layout()

#fig3

f = plt.figure(figsize=(9,9))
grid_spec = f.add_gridspec(3,3)

ax = f.add_subplot(grid_spec[0,0])
sns.distplot(data['adr'], kde=False)

ax = f.add_subplot(grid_spec[0,1])
sns.distplot(data['required_car_parking_spaces'], kde=False)

ax = f.add_subplot(grid_spec[0,-1])
sns.distplot(data['total_of_special_requests'], kde=False)

ax = f.add_subplot(grid_spec[1,0])
sns.distplot(data['adults'], kde=False)

ax = f.add_subplot(grid_spec[1,1])
sns.distplot(data['children'], kde=False)

ax = f.add_subplot(grid_spec[1,-1])
sns.distplot(data['babies'], kde=False)


f.tight_layout()

