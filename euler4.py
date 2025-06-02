numberslist = list(range(1,1000))
products = []
palindromes = []

for x in numberslist:
    for y in numberslist:
        product = x*y
        products.append(product)
        if str(product)== str(product)[::-1]:
            palindromes.append(product)
print(max(palindromes))
    






    
        












