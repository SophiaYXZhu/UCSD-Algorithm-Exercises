# python3

import sys

### naive solution
def check_naive(t1, t2, k):
	assert len(t1) == len(t2)
	mismatch_count = 0
	for i in range(len(t1)):
		if t1[i] != t2[i]:
			mismatch_count += 1
		if mismatch_count > k:
			return False
	return True

def solve_naive(k, text, pattern):
	res = []
	for i in range(len(text) - len(pattern) + 1):
		if check_naive(text[i:i+len(pattern)], pattern, k):
			res.append(i)
	return res

### hashing + binary search solution
prime = 1_000_000_007
multiplier = 263

def solve(k, text, pattern):
	res = []

	hashes_p = [0] * (len(pattern) + 1)
	for i in range(1, len(pattern)+1):
		hashes_p[i] = (multiplier * hashes_p[i-1] + ord(pattern[i-1])) % prime

	hashes_t = [0] * (len(text) + 1)
	for i in range(1, len(text)+1):
		hashes_t[i] = (multiplier * hashes_t[i-1] + ord(text[i-1])) % prime

	for i in range(len(text) - len(pattern) + 1):
		count = 0
		l = i
		r = len(pattern) + i - 1
		while count <= k:
			mismatch_idx = -1
			while l <= r:
				mid = (l+ r) // 2

				hash_left_substr_t = (hashes_t[mid + 1] - pow(multiplier, mid - l + 1, prime) * hashes_t[l]) % prime
				hash_left_substr_p = (hashes_p[mid - i + 1] - pow(multiplier, mid - l + 1, prime) * hashes_p[l - i]) % prime

				if hash_left_substr_t == hash_left_substr_p:
					l = mid + 1
				else:
					mismatch_idx = mid
					r = mid - 1

			if mismatch_idx != -1:
				count += 1
				l = mismatch_idx + 1
				r = len(pattern) + i - 1
			else:
				res.append(i)
				break
	return res

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)