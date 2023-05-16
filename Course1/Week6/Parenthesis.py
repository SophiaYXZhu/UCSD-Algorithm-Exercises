def min_max(M, m, i, j, operators):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = operators[k](M[i][k], M[k+1][j])
        b = operators[k](M[i][k], m[k+1][j])
        c = operators[k](m[i][k], M[k+1][j])
        d = operators[k](m[i][k], m[k+1][j])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(operands, operators):
    n = len(operands)
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = min_max(M, m, i, j, operators)
    return M[0][n-1]

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

expression = input()
operators = []
operands = []
for char in expression:
    if char == "+":
        operators.append(add)
    elif char == "-":
        operators.append(sub)
    elif char == "*":
        operators.append(mul)
    else:
        operands.append(int(char))
print(get_maximum_value(operands, operators))