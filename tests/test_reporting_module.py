import unittest
from src.reporting_module import ReportingModule

class TestReportingModule(unittest.TestCase):
    def setUp(self):
        self.csv_file_path = 'data/claims.csv'
        self.reporting_module = ReportingModule(self.csv_file_path)

    def test_read_claims_data(self):
        claims_data = self.reporting_module.read_claims_data()
        self.assertIsInstance(claims_data, list)
        self.assertGreater(len(claims_data), 0)

    def test_generate_report(self):
        report = self.reporting_module.generate_report()
        self.assertIsInstance(report, dict)
        self.assertIn('total_claims', report)
        self.assertIn('approved_claims', report)
        self.assertIn('rejected_claims', report)

if __name__ == '__main__':
    unittest.main()
