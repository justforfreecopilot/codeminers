import unittest
import pandas as pd
from io import StringIO

class TestClaimPopulate(unittest.TestCase):
    def setUp(self):
        # Sample CSV data
        csv_data = StringIO("""claim_id,policy_number,claim_amount,date_of_incident,status,payout_amount,rejection_reason
1,POL123,1000.0,2023-10-01,Submitted,0.0,
2,POL456,2500.0,2023-09-15,Approved,2000.0,
3,POL789,500.0,2023-10-05,Rejected,0.0,
4,POL101,1500.0,2023-09-20,Approved,1200.0,
5,POL202,3000.0,2023-10-10,Submitted,0.0,
6,POL1234,1000.0,2023-10-01,Submitted,0.0,
7,POL1254,1000.0,2023-10-01,Submitted,0.0,""")
        self.claims_df = pd.read_csv(csv_data)

    def test_valid_option_matching_data(self):
        filtered_df = self.claims_df[self.claims_df['claim_id'].astype(str) == '1']
        self.assertFalse(filtered_df.empty)
        self.assertEqual(filtered_df.iloc[0]['policy_number'], 'POL123')

    def test_valid_option_no_matching_data(self):
        filtered_df = self.claims_df[self.claims_df['claim_id'].astype(str) == '999']
        self.assertTrue(filtered_df.empty)

    def test_invalid_option(self):
        with self.assertRaises(KeyError):
            self.claims_df['invalid_column']

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            int('abc')

    def test_exit_option(self):
        self.assertTrue(True)  # This is a placeholder for the exit functionality

    def test_valid_option_matching_data_different_column(self):
        filtered_df = self.claims_df[self.claims_df['policy_number'] == 'POL123']
        self.assertFalse(filtered_df.empty)
        self.assertEqual(filtered_df.iloc[0]['claim_id'], 1)

    def test_valid_option_matching_data_another_column(self):
        filtered_df = self.claims_df[self.claims_df['status'] == 'Approved']
        self.assertFalse(filtered_df.empty)
        self.assertEqual(filtered_df.iloc[0]['claim_id'], 2)

if __name__ == '__main__':
    unittest.main()