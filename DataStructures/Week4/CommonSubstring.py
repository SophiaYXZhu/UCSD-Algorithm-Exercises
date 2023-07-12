# python3

import sys

def solve(s, t):
    p1 = 1_000_000_007
    p2 = 1_000_000_009
    x = 263
    start_index_s = 0
    start_index_t = 0
    k = 0

    len_s = len(s)
    len_t = len(t)

    # Calculate hash values for string1 and string2
    hash1_s = [0] * (len_s + 1)
    hash2_s = [0] * (len_s + 1)
    hash1_t = [0] * (len_t + 1)
    hash2_t = [0] * (len_t + 1)
    for i in range(1, len_s + 1):
        hash1_s[i] = (hash1_s[i - 1] * x + ord(s[i - 1])) % p1
        hash2_s[i] = (hash2_s[i - 1] * x + ord(s[i - 1])) % p2
    for i in range(1, len_t + 1):
        hash1_t[i] = (hash1_t[i - 1] * x + ord(t[i - 1])) % p1
        hash2_t[i] = (hash2_t[i - 1] * x + ord(t[i - 1])) % p2

    # Binary search to find the longest common substring length
    low = 0
    high = min(len_s, len_t)
    while low <= high:
        mid = (low + high) // 2
        found = False
        hashes_1 = set()
        hashes_2 = set()
        for i in range(len_s - mid + 1):
            hash1 = (hash1_s[i + mid] - hash1_s[i] * pow(x, mid, p1)) % p1
            hashes_1.add(hash1)
            hash2 = (hash2_s[i + mid] - hash2_s[i] * pow(x, mid, p2)) % p2
            hashes_2.add(hash2)
        for j in range(len_t - mid + 1):
            t1 = (hash1_t[j + mid] - hash1_t[j] * pow(x, mid, p1)) % p1
            t2 = (hash2_t[j + mid] - hash2_t[j] * pow(x, mid, p2)) % p2
            if t1 in hashes_1 and t2 in hashes_2:
                found = True
                start_index_t = j
                for q in range(len(s)):
                    if s[q:q+mid] == t[j:j+mid]:
                        start_index_s = q
                        break
                k = mid
                break
        if found:
            low = mid + 1
        else:
            high = mid - 1

    return start_index_s, start_index_t, k
        
for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans[0], ans[1], ans[2])