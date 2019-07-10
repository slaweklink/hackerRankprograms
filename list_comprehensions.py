def kwadrat(n):
    return n*n
def suma(n):
    return n+n

generatorlisty = [[kwadrat(x) for x in range(1,10)], [suma(x) for x in range(10,20)]]

print(generatorlisty)
