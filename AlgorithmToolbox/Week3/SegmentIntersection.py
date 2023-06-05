n = int(input())
segments = []
for i in range(n):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    segments.append(tmp)

points = []
while len(segments) > 0:
    min_idx = 0
    for j in range(len(segments)):
        if segments[j][1] <= segments[min_idx][1]:
            min_idx = j
    p = segments[min_idx][1]
    points.append(p)
    j = 0
    while j >= 0 and j < len(segments):
        if segments[j][0] <= p and segments[j][1] >= p:
            segments.pop(j)
            j -= 1
        j += 1

print(len(points))
for point in points:
    print(point, end=" ")