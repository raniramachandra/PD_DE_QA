import unittest
import pandas as pd
from datetime import datetime
from EDA_Function import calculate_day_diff  # replace with your actual filename (without .py)

class TestCalculateDayDiff(unittest.TestCase):
    
    def test_basic(self):
        """Test basic functionality with valid dates."""
        data = pd.DataFrame({
            'Book checkout': [pd.Timestamp('2025-01-01'), pd.Timestamp('2025-02-10')],
            'Book Returned': [pd.Timestamp('2025-01-05'), pd.Timestamp('2025-02-15')]
        })
        expected = [4, 5]
        result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
        
        self.assertIn('day_diff', result.columns)
        self.assertListEqual(result['day_diff'].tolist(), expected)

    def test_with_nulls(self):
        """Test when one of the dates is missing."""
        data = pd.DataFrame({
            'Book checkout': [pd.Timestamp('2025-01-01'), None],
            'Book Returned': [pd.Timestamp('2025-01-03'), pd.Timestamp('2025-01-05')]
        })
        result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
        
        self.assertTrue(pd.isna(result.loc[1, 'day_diff']))
        self.assertEqual(result.loc[0, 'day_diff'], 2)

    def test_negative_diff(self):
        """Test when return date is before checkout date."""
        data = pd.DataFrame({
            'Book checkout': [pd.Timestamp('2025-01-10')],
            'Book Returned': [pd.Timestamp('2025-01-05')]
        })
        result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
        self.assertEqual(result.loc[0, 'day_diff'], -5)

    def test_empty_dataframe(self):
        """Test when the dataframe is empty."""
        data = pd.DataFrame(columns=['Book checkout', 'Book Returned'])
        result = calculate_day_diff(data, 'Book checkout', 'Book Returned')
        
        self.assertIn('day_diff', result.columns)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
