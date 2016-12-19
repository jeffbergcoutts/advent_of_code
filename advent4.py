f = open('input_4.txt', 'r')
#for line in f:
#    print line

sample_input = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

for line in sample_input:
    print "line: ", line
    line = line.replace('-', '')
    print "line: ", line
    for block in line.split('-'):
        print block
    ID = block.split('[')[0]
    checkSum = block.split('[')[1].replace(']', '')
    print "ID: ", ID
    print "checkSum: ", checkSum
