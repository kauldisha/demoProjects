import csv

with open('product12.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row)
            print(','.join(row))
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} Done {row[1]} in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')