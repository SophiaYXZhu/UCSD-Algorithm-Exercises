# python3

def build_heap_dict(arr, n):
    ans = []
    temp = arr.copy()
	# Dictionary which stores the indexes of the input array
    h = {}
    temp.sort()
    for i in range(n):
        h[arr[i]] = i
    init = 0
    for i in range(n):
		# This is checking whether the current element is at the right place or not
        if (arr[i] != temp[i]):
            ans.append((i, h[temp[i]]))
            init = arr[i]
			# If not, swap this element with the index of the element which should come here
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
            # Update the indexes in the hashmap accordingly
            h[init] = h[temp[i]]
            h[temp[i]] = i
    return ans

def sift_down(i, H, swaps, size):
    min_idx = i
    l = 2 * i + 1
    if l < size and H[l] < H[min_idx]:
        min_idx = l
    r = 2 * i + 2
    if r < size and H[r] < H[min_idx]:
        min_idx = r
    if i != min_idx:
        H[i], H[min_idx] = H[min_idx], H[i]
        swaps.append((i, min_idx))
        sift_down(min_idx, H, swaps, size)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)
    swaps = []
    for i in range(n//2 - 1, -1, -1):
        sift_down(i, data, swaps, n)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()


