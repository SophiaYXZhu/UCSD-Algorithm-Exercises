inp = input().split()
a, b = int(inp[0]), int(inp[1])

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

print(GCD(a, b))