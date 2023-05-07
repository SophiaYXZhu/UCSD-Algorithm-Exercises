n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
keys = [int(i) for i in input().split()]

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

for i in keys:
    print(binary_search(arr, 0, len(arr)-1, i), end=" ")