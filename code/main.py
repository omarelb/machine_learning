# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:36:40 2017

@author: Omar
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

train_df = pd.read_json("../../data/train.json")
print(train_df.head())
