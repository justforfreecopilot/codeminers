import unittest
from src.sid_python import approve_or_reject_claim, save_claim, POLICY_DATA


class TestClaimApproval(unittest.TestCase):

    def setUp(self):
        # Setup a sample claim for testing
        self.sample_claim = {
            "claim_id": 1,
            "policy_number": "P123456",
            "claim_amount": 3000,
            "date_of_incident": "2025-03-01",
            "status": "Submitted",
            "payout_amount": 0.0,
            "rejection_reason": "",
        }
        save_claim(self.sample_claim)

    def test_approve_claim(self):
        result = approve_or_reject_claim(1, "Approved")
        self.assertEqual(result, "Claim updated successfully")

    def test_reject_claim(self):
        result = approve_or_reject_claim(1, "Rejected", "Invalid claim")
        self.assertEqual(result, "Claim updated successfully")

    def test_claim_not_found(self):
        result = approve_or_reject_claim(999, "Approved")
        self.assertEqual(result, "Claim ID not found")


if __name__ == "__main__":
    unittest.main()
