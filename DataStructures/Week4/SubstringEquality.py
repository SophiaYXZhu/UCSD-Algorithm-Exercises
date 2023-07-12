# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.x = 263
		self.m1 = pow(10,9) + 7
		self.m2 = pow(10,9) + 9
		self.cons1 = [1] * (len(s)+1)
		self.cons2 = [1] * (len(s)+1)
		for i in range(1, len(s)+1):
			self.cons1[i] = self.x * self.cons1[i-1] % self.m1
		for i in range(1, len(s)+1):
			self.cons2[i] = self.x * self.cons1[i-1] % self.m2
		self.H1 = [None] * (len(s)+1)
		self.H1[0] = 0
		for i in range(1, len(s)+1):
			self.H1[i] = (self.x * self.H1[i-1] + ord(self.s[i-1])) % self.m1
		self.H2 = [None] * (len(s)+1)
		self.H2[0] = 0
		for i in range(1, len(s)+1):
			self.H2[i] = (self.x * self.H2[i-1] + ord(self.s[i-1])) % self.m2

	def ask(self, a, b, l):
		c1 = self.cons1[l]
		c2 = self.cons2[l]
		Ha1 = ((self.H1[a+l] - c1 * self.H1[a]) % self.m1 + self.m1) % self.m1
		Hb1 = ((self.H1[b+l] - c1 * self.H1[b]) % self.m1 + self.m1) % self.m1
		Ha2 = ((self.H2[a+l] - c2 * self.H2[a]) % self.m2 + self.m2) % self.m2
		Hb2 = ((self.H2[b+l] - c2 * self.H2[b]) % self.m2 + self.m2) % self.m2
		return Ha1 == Hb1 and Ha2 == Hb2


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
