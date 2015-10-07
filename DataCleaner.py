import csv

csvfile = open('cleanme.csv', 'r')
outfile = open('cleanme-clean.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile,reader.fieldnames)

for row in reader:
	row['first_name'] = row['first_name'].upper()
	row['city'] = row['city'].replace('&nbsp;', ' ')
	row['zip'] = row['zip'].zfill(5)

	if len(row['amount']) >= 1000:
		writer.writerow(row)	
