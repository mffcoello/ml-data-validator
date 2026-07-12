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