# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:36:40 2017

@author: Omar
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

color = sns.color_palette()
pd.options.mode.chained_assignment = None  # default='warn'

train_df = pd.read_json("../../data/train.json")
test_df = pd.read_json("../../data/test.json")
#print(train_df.head())


#int_level = train_df['interest_level'].value_counts()
#plt.figure(figsize=(8,4))
#sns.barplot(int_level.index, int_level.values, alpha=0.8, color=color[1])
#plt.ylabel('Number of Occurrences', fontsize=12)
#plt.xlabel('Interest level', fontsize=12)

train_df["interest_level_numerical"] = [mapping[x] for x in train_df["interest_level"].values]

plt.figure()
plt.axes([0,8,0,4])
sns.pairplot(train_df, x_vars=["bedrooms", "bathrooms", "price"],\
             y_vars= "interest_level_numerical", kind="reg")
plt.show()

#print(train_df.head())
