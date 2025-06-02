start = 1
end = 999
number = list(range(start,end+1))
listMRM = []
for x in number:
    rem=x%3
    check = rem == 0
    if check == True:
        listMRM.append(x)
dogs = sum(listMRM)
start = 1
end = 999
mumber = list(range(start,end+1))
listDLM = []
for x in mumber:
    remy=x%5
    check = remy == 0
    if check == True:
        listDLM.append(x)
cats = sum(listDLM)
CandD = set(listMRM+listDLM)
Ferrets = sum(CandD)
print(Ferrets)