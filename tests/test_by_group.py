import pandas as pd
from validator import check_missing_by_group


def test_check_missing_by_group_flags_uneven_missingness():
    df = pd.DataFrame({
        "country": ["US", "US", "US", "US", "FR", "FR", "FR", "FR"],
        "score": [1, 2, 3, 4, None, None, 7, 8],  # missing concentrated in FR
    })

    result = check_missing_by_group(df, group_col="country")

    assert result["FR"]["score"] > result["US"]["score"]
    assert result["US"]["score"] == 0.0