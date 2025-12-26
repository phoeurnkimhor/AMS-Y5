import pandas as pd
from cleaner import clean

def test_clean_removes_duplicates_and_missing_values():
    data = {'A': [1, 1, 2, None], 'B': ['x', 'x', 'y', 'z']}
    df = pd.DataFrame(data)
    cleaned_df = clean(df)
    assert cleaned_df.isnull().sum().sum() == 0
    assert cleaned_df.duplicated().sum() == 0
    expected_df = pd.DataFrame({'A': [1.0, 2.0], 'B': ['x', 'y']})
    pd.testing.assert_frame_equal(cleaned_df.reset_index(drop=True), expected_df)