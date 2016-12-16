coordinates = ["L5", "R1", "R3", "L4", "R3", "R1", "L3", "L2", "R3", "L5", "L1", "L2", "R5", "L1", "R5", "R1", "L4", "R1", "R3", "L4", "L1", "R2", "R5", "R3", "R1", "R1", "L1", "R1", "L1", "L2", "L1", "R2", "L5", "L188", "L4", "R1", "R4", "L3", "R47", "R1", "L1", "R77", "R5", "L2", "R1", "L2", "R4", "L5", "L1", "R3", "R187", "L4", "L3", "L3", "R2", "L3", "L5", "L4", "L4", "R1", "R5", "L4", "L3", "L3", "L3", "L2", "L5", "R1", "L2", "R5", "L3", "L4", "R4", "L5", "R3", "R4", "L2", "L1", "L4", "R1", "L3", "R1", "R3", "L2", "R1", "R4", "R5", "L3", "R5", "R3", "L3", "R4", "L2", "L5", "L1", "L1", "R3", "R1", "L4", "R3", "R3", "L2", "R5", "R4", "R1", "R3", "L4", "R3", "R3", "L2", "L4", "L5", "R1", "L4", "L5", "R4", "L2", "L1", "L3", "L3", "L5", "R3", "L4", "L3", "R5", "R4", "R2", "L4", "R2", "R3", "L3", "R4", "L1", "L3", "R2", "R1", "R5", "L4", "L5", "L5", "R4", "L5", "L2", "L4", "R4", "R4", "R1", "L3", "L2", "L4", "R3"]

direction = 1
x_axis = 0
y_axis = 0
blocks_away = 0
no_of_steps = 0
all_visited = [[0, 0]]
new_visited = []
last_coordinates = [0, 0]
c_all = []

def check_coorindates(a, b):
    for y in a:
        result = y in b
        if result == True:
            print ""
            print "found"
            print y
            print "in"
            print b
            return result

def add_all_coordinates(c1, c2):
    c_all = []
    print "c1", c1, "c2", c2
    a1, b1 = c1
    a2, b2 = c2
    if a1 != a2:
        if a1 > a2:
            for i in range(a2, a1):
                step = [i, b1]
                c_all.append(step)
        elif a1 < a2:
            for i in range(a1, a2):
                step = [i + 1, b1]
                c_all.append(step)
    elif b1 != b2:
        if b1 > b2:
            for i in range(b2, b1):
                step = [a1, i]
                c_all.append(step)
        elif b1 < b2:
            for i in range(b1, b2):
                step = [a1, i + 1]
                c_all.append(step)
    return c_all

for x in coordinates:
    left_or_right = "reset"
    number = "new"
    # split coorindates into direction and # of steps
    for y in list(x):
        if left_or_right == "reset":
            left_or_right = y
        else:
            if number == "new":
                no_of_steps = int(y)
                number = 1
            elif number != "new":
                no_of_steps = int(str(no_of_steps) + str(y))

    # for each set of coordinates move and keep track of where you are and how many blocks away
    if direction == 1:
        if left_or_right == "L":
            direction = 4
            if x_axis <= 0:
                blocks_away = blocks_away + no_of_steps
                x_axis = x_axis - no_of_steps
            elif x_axis > 0:
                blocks_away = blocks_away - no_of_steps
                x_axis = x_axis - no_of_steps
                if x_axis < 0:
                    blocks_away = blocks_away + (abs(x_axis) * 2)
        elif left_or_right == "R":
            direction = 2
            if x_axis >= 0:
                blocks_away = blocks_away + no_of_steps
                x_axis = x_axis + no_of_steps
            elif x_axis < 0:
                blocks_away = blocks_away - no_of_steps
                x_axis = x_axis + no_of_steps
                if x_axis > 0:
                    blocks_away = blocks_away + (x_axis * 2)
    elif direction == 2:
        if left_or_right == "L":
            direction = 1
            if y_axis >= 0:
                blocks_away = blocks_away + no_of_steps
                y_axis = y_axis + no_of_steps
            elif y_axis < 0:
                blocks_away = blocks_away - no_of_steps
                y_axis = y_axis + no_of_steps
                if y_axis > 0:
                    blocks_away = blocks_away + (y_axis * 2)
        elif left_or_right == "R":
            direction = 3
            if y_axis <= 0:
                blocks_away = blocks_away + no_of_steps
                y_axis = y_axis - no_of_steps
            elif y_axis > 0:
                blocks_away = blocks_away - no_of_steps
                y_axis = y_axis - no_of_steps
                if y_axis < 0:
                    blocks_away = blocks_away + (abs(y_axis) * 2)
    elif direction == 3:
        if left_or_right == "L":
            direction = 2
            if x_axis >= 0:
                blocks_away = blocks_away + no_of_steps
                x_axis = x_axis + no_of_steps
            elif x_axis < 0:
                blocks_away = blocks_away - no_of_steps
                x_axis = x_axis + no_of_steps
                if x_axis > 0:
                    blocks_away = blocks_away + (x_axis * 2)
        elif left_or_right == "R":
            direction = 4
            if x_axis <= 0:
                blocks_away = blocks_away + no_of_steps
                x_axis = x_axis - no_of_steps
            elif x_axis > 0:
                blocks_away = blocks_away - no_of_steps
                x_axis = x_axis - no_of_steps
                if x_axis < 0:
                    blocks_away = blocks_away + (abs(x_axis) * 2)
    elif direction == 4:
        if left_or_right == "L":
            direction = 3
            if y_axis <= 0:
                blocks_away = blocks_away + no_of_steps
                y_axis = y_axis - no_of_steps
            elif y_axis > 0:
                blocks_away = blocks_away - no_of_steps
                y_axis = y_axis - no_of_steps
                if y_axis < 0:
                    blocks_away = blocks_away + (abs(y_axis) * 2)
        elif left_or_right == "R":
            direction = 1
            if y_axis >= 0:
                blocks_away = blocks_away + no_of_steps
                y_axis = y_axis + no_of_steps
            elif y_axis < 0:
                blocks_away = blocks_away - no_of_steps
                y_axis = y_axis + no_of_steps
                if y_axis > 0:
                    blocks_away = blocks_away + (y_axis * 2)

    new_coordinates = [x_axis, y_axis]
    new_visited = add_all_coordinates(last_coordinates, new_coordinates)
    result = check_coorindates(new_visited, all_visited)
    if result == True:
        break
    for z in new_visited:
        all_visited.append(z)
    last_coordinates = new_coordinates

print ""
print ""
print "blocks away"
print blocks_away
