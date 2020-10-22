import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')

    with open('new_name.csv', 'w') as new_csv:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_csv, fieldnames = fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

with open('new_name.csv', 'r') as new_csv:
    csv_reader = csv.reader(new_csv, delimiter='\t')

    for line in csv_reader:
        print(line)
