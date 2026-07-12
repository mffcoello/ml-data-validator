import pandas as pd

def check_missing(df: pd.DataFrame, threshold: float = 0.05) -> dict:
    missing_pct = df.isnull().mean()
    flagged = missing_pct[missing_pct > threshold]
    return {
        "missing_pct": missing_pct.to_dict(),
        "flagged_columns": flagged.to_dict(),
    }
def check_imbalance(df: pd.DataFrame, target_col: str, threshold: float = 0.3) -> dict:
    proportions = df[target_col].value_counts(normalize=True)
    minority_ratio = proportions.min()
    return {
        "class_proportions": proportions.to_dict(),
        "is_imbalanced": bool(minority_ratio < threshold),
        "minority_class": proportions.idxmin(),
        "minority_ratio": minority_ratio,
    }
def check_outliers(df: pd.DataFrame, columns: list, multiplier: float = 1.5) -> dict:
    report = {}
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        report[col] = {
            "lower_bound": lower,
            "upper_bound": upper,
            "outlier_count": len(outliers),
        }
    return report