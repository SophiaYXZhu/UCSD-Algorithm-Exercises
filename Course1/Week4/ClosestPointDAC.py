import numpy as np

def dist(p1, p2):
	return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def y_grid(strip, size, d):
	min_dist = d
	strip = sorted(strip, key=lambda point: point[1])
	for i in range(size):
		for j in range(i+1, size):
			if (strip[j][1] - strip[i][1]) >= min_dist:
				break
			if dist(strip[i], strip[j]) < min_dist:
				min_dist = dist(strip[i], strip[j])
	return min_dist

def closest_pair(points, n):
	if n <= 3:
		min_dist = float("inf")
		for i in range(n-1):
			if dist(points[i], points[i+1]) < min_dist:
				min_dist = dist(points[i], points[i+1])
		return min_dist
	mid = n//2
	midPoint = points[mid]
	dl = closest_pair(points, mid)
	dr = closest_pair(points[mid:], n - mid)
	d = min(dl, dr)
	strip = []
	for i in range(n):
		if abs(points[i][0] - midPoint[0]) < d:
			strip.append(points[i])
	return min(d, y_grid(strip, len(strip), d))

n = int(input())
points = []
for i in range(n):
    points.append([int(i) for i in input().split()])
points = sorted(points, key=lambda point: point[0])
print(closest_pair(points, n))