from outlier_function import outlier
import pandas as pd

path = 'data/Study_results.csv'

file = pd.read_csv(path)
pd.DataFrame([file.loc[x] for x in outlier(file['Tumor Volume (mm3)'])['Potential Outliers']])


[x for x in cap['Tumor Volume (mm3)']