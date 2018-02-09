import sys
if len(sys.argv) > 1:
    puzzleInput = int(sys.argv[1])
else:
    print "No Puzzle Input Provided"
    exit()

xAxisValues = [1]
xAxisAddValue = 1
xAxisValue = 1

#create an array that follows the pattern of increasing numbers along the xAxis and stop when you've gone past the input
while True:
    if xAxisValue > puzzleInput:
        break
    xAxisValue = xAxisValue + xAxisAddValue
    xAxisValues.append(xAxisValue)
    xAxisAddValue = xAxisAddValue + 8

#determine how far along the xAxis you went before finding your value
i = len(xAxisValues) - 1

#determine xAxis Values before and after your input
previousxAxisValue = xAxisValues[i - 1]
nextxAxisValue = xAxisValues[i]

#determine distance of circle your input falls in (-1 to account for end of cirlce weirdness)
distanceOfCircle = (nextxAxisValue - previousxAxisValue) - 1

#determine where in the circle your input is in (circle split in eigths)
distanceFromPreviousXAxis = puzzleInput - previousxAxisValue
quadrantSize = (distanceOfCircle) / 4
whichEigth = distanceFromPreviousXAxis / (quadrantSize/2)

#determine the last value in the section your value is in
thisEigthEnd = ((quadrantSize/2) * (whichEigth + 1) + xAxisValues[i - 1])

#determining the distance from the middle only done for the 5th section of the circle
if whichEigth == 5:
    #determine the distance from the center for each axis
    yAxisDistance = i - 1
    xAxisDistance = thisEigthEnd - puzzleInput
    print "Distance: ", yAxisDistance + xAxisDistance
