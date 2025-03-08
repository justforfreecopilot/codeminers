import pandas as pd

# Define the path to the CSV file
file_path = 'data\claims.csv'

# Read the CSV file into a DataFrame
claims_df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(claims_df.head())

# Prompt the user to add input from the specified options
options = ['claim_id', 'policy_number', 'claim_amount', 'date_of_incident', 'status', 'payout_amount', 'rejection_reason', 'Exit']

while True:
    print("Please select an option to add input from the following:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user input
    try:
        selected_option = int(input("Enter the number corresponding to your choice: ")) - 1

        # Ensure the selected option is valid
        if 0 <= selected_option < len(options):
            if options[selected_option] == 'Exit':
                print("Exiting the program.")
                break
            else:
                user_input = input(f"Enter the value for {options[selected_option]}: ")
                filtered_df = claims_df[claims_df[options[selected_option]].astype(str) == user_input]
                
                if not filtered_df.empty:
                    print(f"Filtered data based on {options[selected_option]} = {user_input}:")
                    print(filtered_df)
                else:
                    print("No data found for the given input.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your choice.")