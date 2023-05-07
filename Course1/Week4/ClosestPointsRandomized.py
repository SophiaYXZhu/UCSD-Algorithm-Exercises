import numpy as np
import random

class Grid:
    def __init__(self, p1, p2):
        self.r = np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        self.points = {}
        self.points[self.__boxify(p1, self.r)] = []
        self.points[self.__boxify(p1, self.r)].append(p1)
        if not self.__boxify(p2, self.r) in list(self.points.keys()):
            self.points[self.__boxify(p2, self.r)] = []
        self.points[self.__boxify(p2, self.r)].append(p2)

    def __boxify(self, p, r):
        if r == 0:
            return (p[0], p[1])
        return (p[0]//r, p[1]//r)

    def insert(self, p):
        coor = self.__boxify(p, self.r)
        min_r = self.r
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (coor[0]+i, coor[1]+j) in list(self.points.keys()):
                    for point in self.points[(coor[0]+i, coor[1]+j)]:
                        new_r = np.sqrt((p[0]-point[0])**2+(p[1]-point[1])**2)
                        if new_r < min_r:
                            min_r = new_r
        if min_r < self.r:
            self.r = min_r
            if self.r == 0:
                return 0
            new_points = self.points
            self.points = {}
            for point_arr in list(new_points.values()):
                for point in point_arr:
                    if not self.__boxify(point, self.r) in list(self.points.keys()):
                        self.points[self.__boxify(point, self.r)] = []
                    self.points[self.__boxify(point, self.r)].append(point)
            if not self.__boxify(p, self.r) in list(self.points.keys()):
                self.points[self.__boxify(p, self.r)] = []
            self.points[self.__boxify(p, self.r)].append(p)
        else:
            if not self.__boxify(p, self.r) in list(self.points.keys()):
                self.points[self.__boxify(p, self.r)] = []
            self.points[self.__boxify(p, self.r)].append(p)
        return self.r

def random_cp(points):
    random.shuffle(points)
    grid = Grid(points[0], points[1])
    r = grid.r
    if r == 0:
        return 0
    for i in range(2, len(points)):
        r = grid.insert(points[i])
        if grid.r == 0:
            return 0
    return r

n = int(input())
points = []
for i in range(n):
    points.append([int(i) for i in input().split()])
print(random_cp(points))