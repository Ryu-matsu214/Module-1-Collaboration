'''
Ryunosuke Matsuda
Module 3 Lab - Case Study- Lists, Functions, and Classes.py
That is the program to list up the car information.
'''
class Vehicle:
	def __init__(self, type):
		self.type = type
		
		
	
class Automobile(Vehicle):
	def __init__(self, type, year, make, model, door, roof):
		super().__init__(type)
		self.year = year 
		self.make = make
		
		self.model = model
		self.door = door
		
		self.roof = roof
				
def main():
	type = "car"
	year = input("When did it make: ")
	make = input("Which company made it: ")
	model = input("What's model: ")
	door = input("How many doors does it have: ")
	roof = input("Which roof type does it have, solid or sun roof: ")
		
	car = Automobile(type, year, make, model, door, roof)
			
	print(f"Vehicle type: {type}")
	print(f"Year: {year}")
	print(f"Make: {make}")
	print(f"Model: {model}")
	print(f"Doors: {door}")
	print(f"Roof: {roof}")


main()
		
		
		
	
