def fact_iteration(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n+1):
        x = x*i
    return x

print (fact_iteration(5))

def fact_iter(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

print (fact_iter(5))