file = open('input_dec2.txt', 'r')
input = file.read()
lines = [s.strip() for s in input.splitlines()]
array = []
results = []
for line in lines:
	array.append(line.split("\t"))

def solve(puzzle):
	if puzzle == 1:
		for row in array:
			row = [int(i) for i in row]
			sum = max(row) - min(row)
			results.append(sum)
		total = 0
		for result in results:
			total = total + result
		print total
	elif puzzle == 2:
		for row in array:
			row = [int(i) for i in row]
			print row		

solve(2)
