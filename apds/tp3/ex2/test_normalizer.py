import pandas as pd
from normalizer import normalize_column
import pytest

def test_normalize_values_between_0_and_1():
    df = pd.DataFrame({'score': [10, 20, 30, 40, 50]})
    result = normalize_column(df, 'score')
    assert result['score'].between(0, 1).all(), "Values not in [0, 1] range"

def test_output_length_matches_input():
    df = pd.DataFrame({'score': [5, 10, 15]})
    result = normalize_column(df, 'score')
    assert len(result) == len(df), "Output length doesn't match input"

def test_invalid_column_raises_keyerror():
    df = pd.DataFrame({'value': [1, 2, 3]})
    with pytest.raises(KeyError):
        normalize_column(df, 'missing_column')