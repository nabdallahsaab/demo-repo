# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:37:45 2022

@author: isen
"""

import streamlit as st

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

st.write("Hello !")