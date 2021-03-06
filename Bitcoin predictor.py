# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:52:24 2021

@author: Irfan Sheikh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/WidhyaOrg/datasets/master/bitcoin_dataset.csv")
df.columns

print(df["btc_market_price"][1023])

Corelation=pd.DataFrame(df.corr)
