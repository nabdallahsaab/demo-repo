# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:37:45 2022

@author: isen
"""

import streamlit as st

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
st.write("Hello !")
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
