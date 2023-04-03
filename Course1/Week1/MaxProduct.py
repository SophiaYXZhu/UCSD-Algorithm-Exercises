n = int(input())
seq = input().split()
seq = [int(seq[i]) for i in range(n)]
max1 = -1
max_idx = -1
for i in range(n):
    if seq[i] > max1:
        max1 = seq[i]
        max_idx = i
max2 = -1
for j in range(n):
    if seq[j] > max2 and max_idx != j:
        max2 = seq[j]
print(max1 * max2)