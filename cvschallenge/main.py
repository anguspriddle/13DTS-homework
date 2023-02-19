# This program will take valid and invalid emails and their corresponding usernames and place them in seperate,
# Newly created CSV files.

import csv
import re

def is_valid_email(email):
    # patterns for email address to follow to be valid
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
    return bool(re.match(pattern, email))

# reads in the mock data
with open('MOCK_DATA.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # skips the header

    # Find the index of the "username" and "email" columns
    userName_index = headers.index("userName")
    email_index = headers.index("email")

    # Extract the valid emails and their related usernames
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



