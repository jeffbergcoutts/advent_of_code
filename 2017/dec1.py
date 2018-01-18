file = open('input_dec1.txt', 'r')
input = file.read().strip()

def solve(puzzle):
	lastdigit = 0
	total = 0
	if puzzle == 1:
		firstdigit = 0
		for y in input:
			number = int(y)	
			if number == lastdigit:
				total = total + number
			lastdigit = number
			if firstdigit == 0:
				firstdigit = number

		if firstdigit == lastdigit:
			total = total + firstdigit

		print total
	elif puzzle == 2:
		inputArray = []
		
		for y in input:
			inputArray.append(y)
		
		halfPoint = len(inputArray)/2
		total = 0

		for z, x in enumerate(inputArray):
			a = z + 1 
			number = int(x)
			
			if a > halfPoint:
				noLookup = z - halfPoint
			elif a <= halfPoint:
				noLookup = z + halfPoint		
			compareNo = int(inputArray[noLookup])
			
			if number == compareNo:
				total = total + number

		print total

solve(2)
