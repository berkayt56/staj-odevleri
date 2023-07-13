import numpy as np
import pandas as pd

csv_path = r"C:\Users\toprak\Desktop\iris2.data"  # dataset yolu
csv_data = pd.read_csv(csv_path, delimiter=",", header=None)  # dataset okuma

def norm(col):
    normalized_col = []

    max_value = max(col)
    min_value = min(col)
    for value in col:
        if isinstance(value, (int, float)):
            result = (value - min_value) / (max_value - min_value)
            normalized_col.append(result)
    return normalized_col

def normAll():
    np_data = csv_data.copy()
    for s in range(0, np_data.shape[1]-1):
        col = csv_data.iloc[:, s]
        np_data.iloc[:, s] = norm(col)

    return np_data.values

np_data = normAll()
print(np_data)
print("*************")
print(csv_data)
