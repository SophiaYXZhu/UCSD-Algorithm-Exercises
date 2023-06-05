tmp = input().split()
n = int(tmp[0])
W = int(tmp[1])
w = []
v = []
for i in range(n):
    tmp = input().split()
    v.append(int(tmp[0]))
    w.append(int(tmp[1]))

def find_best_value(v, w):
    best_value = 0
    best_index = -1
    for i in range(len(w)):
        value = v[i]/w[i]
        if value >= best_value:
            best_value = value
            best_index = i
    return best_value, best_index

result = 0
total_weight = 0
while len(w) > 0 and W > 0:
    value, index = find_best_value(v, w)
    weight = min(w[index], W)
    result += weight * value
    W -= weight
    v.pop(index)
    w.pop(index)

print(result)