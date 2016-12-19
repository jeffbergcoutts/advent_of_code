f = open('input_3.txt', 'r')
possible_triangles = 0

def check_no_of_possible_triangles(number1, number2, number3, possible_triangles):
    if number1 + number2 > number3:
        if number2 + number3 > number1:
            if number1 + number3 > number2:
                possible_triangles = possible_triangles + 1
    return possible_triangles

def part1(f, possible_triangles):
    for line in f:
        number1 = 0
        number2 = 0
        number3 = 0
        for number in line.split():
            if number1 == 0:
                number1 = int(number)
            elif number1 != 0 and number2 == 0:
                number2 = int(number)
            elif number2!= 0 and number3 == 0:
                number3 = int(number)

        possible_triangles = check_no_of_possible_triangles(number1, number2, number3, possible_triangles)
    return possible_triangles

def part2(f, possible_triangles):
    linecount = 0
    triangle1 = []
    triangle2 = []
    triangle3 = []
    for line in f:
        linecount = linecount + 1
        numbercount = 0
        for number in line.split():
            numbercount = numbercount + 1
            if numbercount == 1:
                triangle1.append(int(number))
            elif numbercount == 2:
                triangle2.append(int(number))
            elif numbercount == 3:
                triangle3.append(int(number))

        if linecount == 3:
            possible_triangles = check_no_of_possible_triangles(triangle1[0], triangle1[1], triangle1[2], possible_triangles)
            possible_triangles = check_no_of_possible_triangles(triangle2[0], triangle2[1], triangle2[2], possible_triangles)
            possible_triangles = check_no_of_possible_triangles(triangle3[0], triangle3[1], triangle3[2], possible_triangles)
            linecount = 0
            triangle1 = []
            triangle2 = []
            triangle3 = []

    return possible_triangles

#possible_triangles = part1(f, possible_triangles)
#print ""
#print "part1", possible_triangles

possible_triangles = part2(f, possible_triangles)

print ""
print "part2", possible_triangles
