import pandas as pd

df = pd.read_csv("data/students_dropout.csv", sep=";")

print(df.shape)
print(df.columns.tolist())
print(df["Target"].value_counts())
print(df.isnull().sum())