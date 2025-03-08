# Reporting Module
# Generates reports on claim statistics (e.g., total claims, approved claims, rejected claims).
# Reads data from the CSV file to generate reports.

import csv

class ReportingModule:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def read_claims_data(self):
        claims_data = []
        with open(self.csv_file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                claims_data.append(row)
        return claims_data

    def generate_report(self):
        claims_data = self.read_claims_data()
        total_claims = len(claims_data)
        approved_claims = len([claim for claim in claims_data if claim['status'] == 'approved'])
        rejected_claims = len([claim for claim in claims_data if claim['status'] == 'rejected'])

        report = {
            'total_claims': total_claims,
            'approved_claims': approved_claims,
            'rejected_claims': rejected_claims
        }
        return report
