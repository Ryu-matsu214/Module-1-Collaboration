#1
secret = 7
guess = 7
if secret > guess:
	print('too low.')
elif secret < guess:
	print('too high')
else:
	print('just right')
	
#2
small = 'false'
green = 'false'
if small == 'true':
	if green == 'true':
		print('pea')
	else:
		print('cherry')
else: 
	if green == 'true':
		print('watermwlon')
	else:
		print('pumpkin')

#3
for count in range(3,-1,-1):
	print(count)

#4
guess_me = 7
number = 1
while guess_me != number:
	if guess_me > number:
		print('too low')
	elif guess_me == number:
		print('found it!')
		break
	else:
		print('Oops')
		break
	number += 3
if guess_me == number:
	print('found it!')

#5
guess_me = 5
for number in range(1, 10, 3):
	if guess_me > number:
		print('too low')
	elif guess_me == number:
		print('found it')
		break
	else:
		print('oops')
		break
	
	
	