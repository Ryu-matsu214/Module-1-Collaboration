import zoo as menagerie

menagerie.hours()
print()
menagerie.holidayHours()







import csv

with open('books.csv', newline = '') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['author'], row['book']) 
				
				
import csv
import sqlite3

conn = sqlite3.connect('books2.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTs books2(
					title TEXT,
					author TEXT,
					year INTEGER
										)
			''')
with open('books2.csv', 'r') as file:
	csv_reader = csv.reader(file)
	next(csv_reader) #skip headerrow if it exists
	for row in csv_reader:
		cursor.execute('INSERT INTO books2 VALUES(?,?,?)', row)
		
conn.commit()
conn.close()