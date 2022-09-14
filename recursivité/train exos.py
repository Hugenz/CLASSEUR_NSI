def fact_iter(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

# print(fact_iter(5))


def fact_rec(n):
    if n <= 1:
        return 1
    return n*fact_iter(n-1)

print(fact_rec(7))
