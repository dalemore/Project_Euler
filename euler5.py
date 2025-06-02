starter_num = 1000000

one_to_20 = list(range(1,20+1))

goodnumbers = []

badnumbers = []

while starter_num < 1000000000:
    startnumdivx = []

    for x in one_to_20:
        if starter_num%x == 0:
            startnumdivx.append(x)

    if sum(startnumdivx) == 210:
        goodnumbers.append(starter_num)
    else:
        badnumbers.append(starter_num)
            
    starter_num += 10 

print(goodnumbers[0])





# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
