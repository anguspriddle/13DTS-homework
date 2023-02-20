# This program will take valid and invalid emails and their corresponding usernames and place them in seperate,
# Newly created CSV files.

import csv
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$' # The pattern listed follows the normal email conventions
def is_valid_email(email):
    # checks the email is valid to pattern mentioned before
    return bool(re.match(pattern, email))

def add_email_to_csv(filename, username, email):
    # Function to add a new email
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, email])

def login():
    valid_data = []
    with open('valid_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            valid_data.append(row)

    username = input("Enter your username: ")
    email = input("Enter your email address: ")

    if not re.match(pattern, email):
        print("Invalid email address.")
        return

    for row in valid_data:
        if row[0] == username and row[1] == email:
            print("Logged in.")
            return

    while True:
        response = input("Username and email combination not found. Try again or create a new account? (try/create/quit): ")
        if response == "try":
            login()
            return
        elif response == "create":
            if re.match(pattern, email):
                with open('valid_data.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([username, email])
                print("Account created.")
                return
            else:
                print("Invalid email address.")
        elif response == "quit":
            return
        else:
            print("Invalid input. Please try again.")


# reads in the mock data
with open('MOCK_DATA.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # skips the header

    # Finds the index of the "username" and "email" columns
    userName_index = headers.index("userName")
    email_index = headers.index("email")

    # Extracts the valid emails and their related usernames
    valid_data = []
    invalid_data = []
    for row in reader:
        email = row[email_index]
        if is_valid_email(email):
            valid_data.append((row[userName_index], email))
        else:
            invalid_data.append((row[userName_index], email))

# Writes only the valid data to a new CSV file
with open('valid_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["username", "email"])
    writer.writerows(valid_data)

# Write only the invalid data to a new CSV file
with open('invalid_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["username", "email"])
    writer.writerows(invalid_data)

login() # runs main login function



