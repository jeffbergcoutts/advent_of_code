file = open('/Users/bergcoutts/advent_of_code/2017/input_dec2.txt', 'r')
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
        total = 0
        for row in array:
            row = [int(i) for i in row]
            for i, val in enumerate(row):
                for n in range(len(row)-(i+1)):
                    number1 = row[i]
                    number2 = row[i+(n+1)]
                    div1 = number2 / float(number1)
                    div2 = number1 / float(number2)
                    if div1.is_integer():
                        total = total + div1
                    if div2.is_integer():
                        total = total + div2
        print total

solve(2)
