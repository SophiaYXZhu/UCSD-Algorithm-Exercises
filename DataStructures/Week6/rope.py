# python3

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
		# In the below implementation, I simply used the python string slices, because it inherently used BSTs.
		# However, the idea is simple:
		# l = OrderStatistics(root, i)
		# r = OrderStatistics(root, j)
		# left, middle = split(root, l)
		# middle, right = split(middle, r)
		# remaining_tree = merge(left, right)
		# insert_idx = OrderStatistics(root, k)
		# remaining_left, remaining_right = split(remaining_tree, insert_idx)
		# root = merge(merge(remaining_left, middle), remaining_right)

		substr = self.s[i:j+1]
		self.s = self.s[:i] + self.s[j+1:]
		if k == 0:
			self.s = substr + self.s
		else:
			self.s = self.s[:k] + substr + self.s[k:]
		
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
