inp = input().split()
n, m = int(inp[0]), int(inp[1])

def pisano_period(m):
    a, b = 0, 1
    for i in range(0, m**2):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1

def fib(n, m):
    period = pisano_period(m)
    n = n % period
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        a, b = b, a + b
    return (b % m)

print(fib(n, m))