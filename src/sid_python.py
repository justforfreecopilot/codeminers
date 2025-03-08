import csv
import os
from datetime import datetime

# Get the absolute path to the data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Path to the src folder
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "claims.csv")

# Example policy data for validation purposes
POLICY_DATA = {
    "P123456": {"coverage": 10000, "claim_limit": 5000},
    "P654321": {"coverage": 20000, "claim_limit": 10000},
    # Add more policies as needed
}


def submit_claim(policy_number, claim_amount, date_of_incident):
    if not validate_claim_data(policy_number, claim_amount, date_of_incident):
        return "Invalid claim data"

    claim_id = get_next_claim_id()
    claim = {
        "claim_id": claim_id,
        "policy_number": policy_number,
        "claim_amount": claim_amount,
        "date_of_incident": date_of_incident,
        "status": "Submitted",
        "payout_amount": 0.0,
        "rejection_reason": "",
    }
    save_claim(claim)
    process_claim(claim)
    return "Claim submitted successfully"


def validate_claim_data(policy_number, claim_amount, date_of_incident):
    if not isinstance(policy_number, str) or not policy_number:
        print("Invalid policy number")
        return False
    if not isinstance(claim_amount, (int, float)) or claim_amount <= 0:
        print("Invalid claim amount")
        return False
    try:
        datetime.strptime(date_of_incident, "%Y-%m-%d")
    except ValueError:
        print("Invalid date of incident")
        return False

    # Validate against business rules
    if policy_number not in POLICY_DATA:
        print("Policy number not found")
        return False
    policy = POLICY_DATA[policy_number]
    if claim_amount > policy["claim_limit"]:
        print("Claim amount exceeds policy claim limit")
        return False

    return True


def get_next_claim_id():
    if not os.path.exists(DATA_FILE):
        return 1
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        claims = list(reader)
    return len(claims) + 1


def save_claim(claim):
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Check if the file exists
    file_exists = os.path.exists(DATA_FILE)

    # Append the claim to the file
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=claim.keys())
        if not file_exists:
            writer.writeheader()  # Write header if the file is new
        writer.writerow(claim)  # Write the claim as a new row


def process_claim(claim):
    policy = POLICY_DATA[claim["policy_number"]]
    if claim["claim_amount"] <= policy["claim_limit"]:
        claim["status"] = "Approved"
        claim["payout_amount"] = claim["claim_amount"]
    else:
        claim["status"] = "Rejected"
        claim["rejection_reason"] = "Claim amount exceeds policy claim limit"

    update_claim(claim)


def update_claim(updated_claim):
    claims = []
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["claim_id"]) == updated_claim["claim_id"]:
                claims.append(updated_claim)
            else:
                claims.append(row)

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=updated_claim.keys())
        writer.writeheader()
        writer.writerows(claims)


def approve_or_reject_claim(claim_id, status, rejection_reason=""):
    claims = []
    claim_found = False
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["claim_id"]) == claim_id:
                row["status"] = status
                row["rejection_reason"] = rejection_reason
                claim_found = True
            claims.append(row)

    if not claim_found:
        return "Claim ID not found"

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=claims[0].keys())
        writer.writeheader()
        writer.writerows(claims)

    return "Claim updated successfully"
