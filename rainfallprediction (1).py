# -*- coding: utf-8 -*-
"""rainfallprediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UIp3KXPPLKoSQNtbJOPb-eBr7mznlR0H
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/content/aws_device_frmpayload_data_rain.csv")

data.info()

data['time'] = pd.to_datetime(data['time'])

data.head()

data.tail()

data.isnull().sum()

Location_1 = 'DVM_NNM_HSS_Maranalloor_Kattakkada'
new_df_1 = data[data['device_name'] == Location_1]
#new_df_1.reset_index(drop=True, inplace=True)
print(new_df_1)

print (new_df_1['time'])
print (new_df_1['value'])

x1= (new_df_1['time'])
y1= (new_df_1['value'])

plt.xlabel('time')
plt.ylabel('value')
plt.plot(x1,y1)

desired_year = 2021
filtered_x1 = [date for date in x1 if date.year == desired_year]
filtered_y1 = [y for date, y in zip(x1, y1) if date.year == desired_year]

plt.plot(filtered_x1, filtered_y1)

plt.xlabel('year')
plt.ylabel('value')

plt.show()

desired_year = 2022
filtered_x1 = [date for date in x1 if date.year == desired_year]
filtered_y1 = [y for date, y in zip(x1, y1) if date.year == desired_year]

plt.plot(filtered_x1, filtered_y1)

plt.xlabel('year')
plt.ylabel('value')

plt.show()

desired_year = 2023
filtered_x1 = [date for date in x1 if date.year == desired_year]
filtered_y1 = [y for date, y in zip(x1, y1) if date.year == desired_year]

plt.plot(filtered_x1, filtered_y1)

plt.xlabel('year')
plt.ylabel('value')

plt.show()

Location_2 = 'Govt_HSS_Vilavoorkkal_Malayam'
new_df_2 = data[data['device_name'] == Location_2]
#new_df.reset_index(drop=True, inplace=True)
print(new_df_2)

print (new_df_2['time'])
print (new_df_2['value'])

x2= (new_df_2['time'])
y2= (new_df_2['value'])

plt.xlabel('time')
plt.ylabel('value')
plt.plot(x2,y2)



Location_3 = 'Govt_Vocational_Girls_HSS_Malayinkeezhu'
new_df_3 = data[data['device_name'] == Location_3]
#new_df.reset_index(drop=True, inplace=True)
print(new_df_3)

x3= (new_df_3['time'])
y3= (new_df_3['value'])
plt.xlabel('time')
plt.ylabel('value')
plt.plot(x3,y3)

Location_4 = 'VVHSS_Nemom'
new_df_4 = data[data['device_name'] == Location_4]
print(new_df_4)

x4= (new_df_4['time'])
y4= (new_df_4['value'])
plt.xlabel('time')
plt.ylabel('value')
plt.plot(x4,y4)

Location_5 = 'Kulathummal_Govt_HSS_Kattakkada'
new_df_5 = data[data['device_name'] == Location_5]
print(new_df_5)

x5= (new_df_5['time'])
y5= (new_df_5['value'])
plt.xlabel('time')
plt.ylabel('value')
plt.plot(x5,y5)

Location_6 = 'Kulathummel_Govt_HSS_Kattakkada'
new_df_6 = data[data['device_name'] == Location_6]
print(new_df_6)

x6= (new_df_6['time'])
y6= (new_df_6['value'])
plt.xlabel('time')
plt.ylabel('value')
plt.plot(x6,y6)

Location_7 = 'St_Xaviers_HSS_Peyad'
new_df_7 = data[data['device_name'] == Location_7]
print(new_df_7)

x7= (new_df_7['time'])
y7= (new_df_7['value'])
plt.xlabel('time')
plt.ylabel('value')
plt.plot(x7,y7)