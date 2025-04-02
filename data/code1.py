# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:25:37 2024

@author: pc
"""
import pandas as pd
import numpy as np

data=pd.read_csv("data.csv",encoding="latin-1")

data_norway=data[data.Country=="Norway"]

data_outlier=data[(data.Quantity>=np.mean(data.Quantity)+3*np.std(data.Quantity)) | (data.Quantity<=np.mean(data.Quantity)-3*np.std(data.Quantity))]

