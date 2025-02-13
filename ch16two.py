import csv

with open('books.csv', newline = '') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['author'], row['book']) 