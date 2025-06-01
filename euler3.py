import math
number = 600851475
start = 2
end =  (number)
truefactors = []
primefactors = []
possiblefactors = list(range(start,round(end)))
for x in possiblefactors:
    rem=number%x 
    check = rem == 0
    if check == True:
        truefactors.append(x)


for factor in truefactors:
    factorfactors = list(range(2,factor))
    prime = True
    for divisor in factorfactors:
        if factor%divisor == 0:
            prime = False

    if prime:
        primefactors.append(factor)

print(primefactors[-1])




