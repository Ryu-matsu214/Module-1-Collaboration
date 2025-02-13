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