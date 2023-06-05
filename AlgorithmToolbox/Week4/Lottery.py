tmp = input().split()
n = int(tmp[0])
m = int(tmp[1])
points = []
for i in range(n):
    tmp = [int(i) for i in input().split()]
    points.append([tmp[0], 'S'])
    points.append([tmp[1], 'E'])
search_points = [int(i) for i in input().split()]
idx = 0
for i in search_points:
    points.append([i, 'P', idx])
    idx += 1

def find_overlap(points):
    count = 0
    count_arr = [-1] * m
    for i in range(0, len(points)):
        if points[i][1] == 'S':
            count += 1
        elif points[i][1] == 'E':
            count -= 1
        else:
            count_arr[points[i][2]] = count
    return count_arr

points.sort(key=lambda x: (x[0], -ord(x[1])))
count_arr = find_overlap(points)
for count in count_arr:
    print(count, end = " ")