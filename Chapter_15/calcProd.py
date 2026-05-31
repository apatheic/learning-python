import time
def calcProd():
    product = 1
    for i in range(1, 1000):
        product *= i
    return product

start = time.time()
prod = calcProd()
end = time.time()
print("Result lenght: %s numbers." % (len(str(prod))))
print('The calculation took %s seconds.' %(end - start))
