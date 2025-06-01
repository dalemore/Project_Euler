lastnum = 0
curnum = 1
nextnum = 0
total = 0
while nextnum < 4000000:
    nextnum = lastnum + curnum
    lastnum = curnum
    curnum = nextnum
    if (curnum%2 == 0):
        total = total+curnum
print(total)
    



