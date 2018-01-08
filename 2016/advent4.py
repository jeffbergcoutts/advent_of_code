import math
f = open('input_4.txt', 'r')
sample_input = ['bbb-aaaaa-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
sample_name = 'qzmt-zixmtkozy-ivhz-343'

def getAllRealRooms(f):
    sumofIds = 0
    for line in f:
        useBlock = ""
        useLetters = []
        for block in line.split('-'):
            for letter in list(useBlock):
                useLetters.append(letter)
            useBlock = block

        ID = block.split('[')[0]
        checkSum = block.split('[')[1].replace(']', '')

        orderedLetters = []
        for letter in useLetters:
            addedLetterAlready = (letter, useLetters.count(letter)) in orderedLetters
            if addedLetterAlready != True:
                orderedLetters.append((letter, useLetters.count(letter)))

        sortedAlphabetically = sorted(orderedLetters)
        sortedAlphabetically.sort(key=lambda x: x[1], reverse=True)
        sortedLetters = ""
        for sortedLetter in sortedAlphabetically:
            sortedLetters += sortedLetter[0]
        sortedLetters = sortedLetters[:5]
        checkSum = checkSum[:5]

        if sortedLetters == checkSum:
            sumofIds = sumofIds + int(ID)
            string = ''.join(useLetters)
            realRoomNames = decodeRoomNames(string, int(ID))
            print "Real room names: ", realRoomNames, ID

    return sumofIds

def decodeRoomNames(room_name_encoded, ID):
    a = int(ID - (26  * (math.floor(ID / 26))))
    string = 'abcdefghijklmnopqrstuvwxyz'
    room_name = []
    for letter in room_name_encoded:
        l = str(letter)
        b = int(string.index(l) + a)
        if b > 25:
            room_name.append(string[b - 26])
        else:
            room_name.append(string[b])
    return ''.join(room_name)

allRealRooms = getAllRealRooms(f)
print "Sum of Sectors ID's", allRealRooms
