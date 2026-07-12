import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.read_csv("data/students_dropout.csv", sep=";")

cols_to_dirty = ["Admission grade", "Previous qualification (grade)", "Mother's occupation"]
missing_fraction = 0.03

for col in cols_to_dirty:
    mask = np.random.rand(len(df)) < missing_fraction
    df.loc[mask, col] = np.nan

df.to_csv("data/students_dropout_dirty.csv", sep=";", index=False)

print(df.isnull().sum()[df.isnull().sum() > 0])