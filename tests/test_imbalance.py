import pandas as pd
from validator import check_imbalance


def test_check_imbalance_flags_skewed_classes():
    df = pd.DataFrame({"target": ["A"] * 80 + ["B"] * 20})

    result = check_imbalance(df, target_col="target", threshold=0.3)

    assert result["is_imbalanced"] is True
    assert result["minority_class"] == "B"


def test_check_imbalance_passes_balanced_classes():
    df = pd.DataFrame({"target": ["A"] * 50 + ["B"] * 50})

    result = check_imbalance(df, target_col="target", threshold=0.3)

    assert result["is_imbalanced"] is False