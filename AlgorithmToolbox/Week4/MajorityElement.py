n = int(input())
arr = [int(i) for i in input().split()]

counts = {}
for i in arr:
    try:
        counts[i] += 1
    except KeyError:
        counts[i] = 1

for i in counts:
    if counts[i] > n//2:
        print(1)
        exit(0)
print(0)