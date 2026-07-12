import pandas as pd
from validator import check_missing


def test_check_missing_flags_column_above_threshold():
    df = pd.DataFrame({
        "a": [1, 2, None, None, 5],   # 40% missing
        "b": [1, 2, 3, 4, 5],         # 0% missing
    })

    result = check_missing(df, threshold=0.05)

    assert "a" in result["flagged_columns"]
    assert "b" not in result["flagged_columns"]


def test_check_missing_returns_zero_for_clean_column():
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})

    result = check_missing(df, threshold=0.05)

    assert result["missing_pct"]["a"] == 0.0