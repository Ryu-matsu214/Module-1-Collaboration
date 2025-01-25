"""
Ryunosuke Matsuda
Identifying GPA with student's names
That is the app that I divide each student by their GPA
"""
lName = ""
fName = ""
fullName = ""
GPA = 0.0

lName = input("Please enter student's Last Name. If you want to quit, enter ZZZ:  ")

while lName != "ZZZ":
	fName = input("Please enter your First Name: ")
	GPA = float(input('what is the GPA that ' + fName + ' '+ lName + ' has: '))
	fullName = fName + lName
	if GPA >= 3.5:
		print(fullName + " is the Dean's List" )
	elif GPA >= 3.25:
		print(fullName + " is the Honor Roll" )
	else:
		print(fullName + " is none.")
	lName = input("Please enter student's Last Name. If you want to quit, enter ZZZ:  ")
	lName = lName.upper()

	
 
		
