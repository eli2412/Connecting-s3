import unittest
import main

class TestConfig(unittest.TestCase):

  def test_merged_data_values(self):
    # Assert that the merged_data contains values stored in the two CSV files
    self.assertEqual(main.merged_data.iloc[0].GRE_Score, 337.0)
    self.assertEqual(main.merged_data.iloc[0]['Chance_of_Admit'], 0.92)
    self.assertEqual(main.merged_data.iloc[412].GRE_Score, 329.00)
    self.assertEqual(main.merged_data.iloc[412]['Chance_of_Admit'], 0.89)
  
  def test_cleaned_data_values(self):
    # Assert that empty rows have been removed from the file.
    # Should have 405 rows
    self.assertEqual(len(main.cleaned_data), 405)
    # merged_data should have rows of NaN whereas cleaned_data should not
    self.assertEqual(main.cleaned_data.isna().values.any(), False)
    self.assertEqual(main.merged_data.isna().values.any(), True)

    
if __name__ == '__main__':
  unittest.main()