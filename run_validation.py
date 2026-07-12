import pandas as pd
from validator import check_missing, check_imbalance, check_outliers

df = pd.read_csv("data/students_dropout_dirty.csv", sep=";")

print("=== Missing Values ===")
missing_report = check_missing(df, threshold=0.01)
for col, pct in missing_report["flagged_columns"].items():
    print(f"{col}: {pct:.1%} missing")

print("\n=== Class Imbalance ===")
imbalance_report = check_imbalance(df, target_col="Target", threshold=0.3)
print(f"Imbalanced: {imbalance_report['is_imbalanced']}")
print(f"Minority class: {imbalance_report['minority_class']} ({imbalance_report['minority_ratio']:.1%})")

print("\n=== Outliers ===")
outlier_report = check_outliers(df, columns=["Age at enrollment"])
for col, stats in outlier_report.items():
    print(f"{col}: {stats['outlier_count']} outliers (bounds: {stats['lower_bound']:.1f} to {stats['upper_bound']:.1f})")