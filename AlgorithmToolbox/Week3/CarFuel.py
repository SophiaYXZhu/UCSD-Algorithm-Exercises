d = int(input())
m = int(input())
n = int(input())
tmp = input().split()
stops = []
for i in range(n):
    stops.append(int(tmp[i]))

count, idx, total_dist = 0, 0, m
while total_dist < d:
    if idx >= n or stops[idx] > total_dist:
        print(-1)
        exit(0)
    while idx < n-1 and stops[idx+1] <= total_dist:
        idx += 1
    total_dist = stops[idx] + m
    idx += 1
    count += 1
print(count)

