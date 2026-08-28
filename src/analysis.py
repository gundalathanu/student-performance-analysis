import pandas as pd

data = pd.read_csv("../data/students.csv")

print("First five rows:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nStatistical summary:")
print(data.describe())

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())