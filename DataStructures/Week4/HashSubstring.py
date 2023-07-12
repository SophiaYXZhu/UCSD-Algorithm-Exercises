# python3

p = 1000000007
x = 263

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = ((ans * x + ord(c)) % p + p) % p
    return ans

def preprocess(pattern, text):
    H = [None] * (len(text) - len(pattern) + 1)
    S = text[len(text)-len(pattern):]
    H[len(text) - len(pattern)] = _hash_func(S)
    y = 1
    for i in range(len(pattern)):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        H[i] = ((x * H[i+1] + ord(text[i]) - y * ord(text[i+len(pattern)])) % p + p) % p
    return H

def get_occurrences(pattern, text):
    positions = []
    p_hashed = _hash_func(pattern)
    H = preprocess(pattern, text)
    for i in range(len(text) - len(pattern)+1):
        if p_hashed != H[i]:
            continue
        elif pattern == text[i:i+len(pattern)]:
            positions.append(i)
    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))