import pandas as pd
from validator import check_outliers


def test_check_outliers_detects_extreme_value():
    df = pd.DataFrame({"age": [20, 21, 22, 23, 24, 25, 70]})  # 70 is way out

    result = check_outliers(df, columns=["age"])

    assert result["age"]["outlier_count"] == 1


def test_check_outliers_no_outliers_in_uniform_data():
    df = pd.DataFrame({"age": [20, 21, 22, 23, 24, 25, 26]})

    result = check_outliers(df, columns=["age"])

    assert result["age"]["outlier_count"] == 0