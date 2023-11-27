import csv

with open("studentslist.csv", 'r', encoding='utf-8') as csvfile:
    # Create a CSV reader object with header
    csv_reader = csv.DictReader(csvfile)

    # Iterate through rows in the CSV file as dictionaries
    for row in csv_reader:
        if int(row['age']) < 30:
            print(row['first_name'] + " " + row['last_name'] + " " + row['email'])