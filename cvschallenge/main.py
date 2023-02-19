import csv
import re

# Makes a variable for what a normal email expression would be
email_regex = r"[^@]+@[^@]+\.[^@]+"

# Open the input and output files
with open('MOCK_DATA.csv', 'r') as infile, open('valid_emails.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row to the output file
    writer.writerow(['username', 'email'])

    # Loop through each row of the input file
    for row in reader:
        try:
            userName, email = row
            print(row)
        except ValueError:
            continue

        # Checks if the email is valid
        if re.match(email_regex, email):
            # Write the validated email with it's username into the other file
            writer.writerow([userName, email])
