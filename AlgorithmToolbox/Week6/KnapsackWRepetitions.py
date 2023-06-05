def compute_table(weights, values, capacity):
    assert len(weights) == len(values)
    table = [0] * (capacity + 1)
    for i in range(1, capacity + 1):
        max_value = table[i-1]
        for j in range(len(weights)):
            if weights[j] <= i:
                value = table[i-weights[j]] + values[j]
                if max_value < value:
                    max_value = value
        table[i] = max_value
    return table[capacity]

capacity = int(input())
n = int(input())
weights = []
values = []
for i in range(n):
    tmp = input().split()
    weights.append(int(tmp[0]))
    values.append(int(tmp[1]))
print(compute_table(weights, values, capacity))