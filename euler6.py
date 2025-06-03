onetohundred = list(range(1,100+1))
onetohundredsqrd = list()

# This function squares every element of the range
def sumsquares(n):
    return [x**2 for x in range(1, n + 1)]


# This function squares the sum of all the elements in the range
def squaresum(n):
    return sum(range(1, n + 1))**2

#This function subtracts the two 
difference = squaresum(100) - sum(sumsquares(100))

print(difference)



# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.