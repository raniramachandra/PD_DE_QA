
import pytest
import pandas as pd
from datetime import datetime
from EDA_function import calculate_day_diff  # replace with your actual module name

def test_calculate_day_diff_basic():
    # Create sample input DataFrame
    data = pd.DataFrame({
        'Book checkout': [pd.Timestamp('2025-01-01'), pd.Timestamp('2025-02-10')],
        'Book Returned': [pd.Timestamp('2025-01-05'), pd.Timestamp('2025-02-15')]
    })
    
    # Expected day difference
    expected_days = [4, 5]
    
    # Apply function
    result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
    
    # Assertions
    assert 'day_diff' in result.columns, "Missing 'day_diff' column in result"
    assert result['day_diff'].tolist() == expected_days, f"Expected {expected_days}, got {result['day_diff'].tolist()}"

def test_calculate_day_diff_with_nulls():
    # Data with missing dates
    data = pd.DataFrame({
        'Book checkout': [pd.Timestamp('2025-01-01'), None],
        'Book Returned': [pd.Timestamp('2025-01-03'), pd.Timestamp('2025-01-05')]
    })
    
    result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
    
    # The first should be 2 days, second should be NaN
    assert pd.isna(result.loc[1, 'day_diff']), "Expected NaN for missing checkout date"
    assert result.loc[0, 'day_diff'] == 2, "Expected 2 days difference for first record"

def test_calculate_day_diff_negative():
    # Case where return date is before checkout date
    data = pd.DataFrame({
        'Book checkout': [pd.Timestamp('2025-01-10')],
        'Book Returned': [pd.Timestamp('2025-01-05')]
    })
    
    result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
    
    # Should result in negative day difference
    assert result.loc[0, 'day_diff'] == -5, "Expected -5 days difference"

def test_calculate_day_diff_empty_dataframe():
    # Empty dataframe should still return with a day_diff column
    data = pd.DataFrame(columns=['Book checkout', 'Book Returned'])
    result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
    
    assert 'day_diff' in result.columns, "Expected 'day_diff' column even for empty dataframe"
    assert len(result) == 0, "Expected result to have zero rows"

