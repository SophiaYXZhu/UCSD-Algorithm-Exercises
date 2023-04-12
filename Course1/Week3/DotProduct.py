n = int(input())
v1 = []
v2 = []
tmp = input().split()
for i in range(n):
    v1.append(int(tmp[i]))
tmp = input().split()
for i in range(n):
    v2.append(int(tmp[i]))

def max_product(v1, v2):
    m1 = max(v1)
    idx1 = v1.index(m1)
    m2 = max(v2)
    idx2 = v2.index(m2)
    return m1, idx1, m2, idx2

sum = 0
for i in range(n):
    m1, idx1, m2, idx2 = max_product(v1, v2)
    sum += m1*m2
    v1.pop(idx1)
    v2.pop(idx2)

print(sum)
