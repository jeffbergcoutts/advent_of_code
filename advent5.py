import hashlib

doorID = 'abbhdwsy'
a = 0
found = 0
stop = False

while stop != True:
    a = a + 1
    thisdoorID = doorID + str(a)
    m = hashlib.md5(thisdoorID).hexdigest()
    if m.startswith('00000'):
        print m[5]
        found = found + 1
        if found == 8:
            stop = True

answer = '801b56a7'
