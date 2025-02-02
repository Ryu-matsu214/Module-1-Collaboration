things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize()
print(things)  

things[0] = things[0].upper()
print(things)  

things.remove("salmonella")
things.append("Win a compitition.")
print(things) 


list = []
def good():
	list.append("Harry")
	list.append("Ron")
	list.append("Hermonie")
	return list
	
good()

print(list)

list_odd = []
list_even = []
def get_odds():
	num = 0
	num1 = 0
	for num in range(10):
		num1 = num % 2
		if num1 == 0:
			list_even.append(num)
		else:
			list_odd.append(num)
			
		num += 1

get_odds()

print(list_odd)
		

			
		




