f = open('input_4.txt', 'r')
sample_input = ['bbb-aaaaa-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
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

print "Sum of Sectors ID's", sumofIds
