arr = [0, 1, 2, 0, 2, 1]

arr2 = []

count = 0
count2 = count + 1

for count in range((len(arr))):
	for (count2) in range(len(arr)):
		if arr[count] < arr[count2]:
			temp = -99
			temp = arr[count]
			arr[count] = arr[count2]
			arr[count2] = temp
		temp = -99
		
print(arr)



numToFind = 4

myList = [1, 2, 3, 4, 5]

for count in range(len(myList)):
	if numToFind == myList[count]:
		myIndex = count
		
if myIndex == '':
	print(f'{numToFind} is not present.')
	
else:
	print(f'{numToFind} appears at {myIndex}')	