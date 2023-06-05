import random

n = int(input())
arr = [int(i) for i in input().split()]

def partition3(arr, l, r):
    m1 = l
    i = l+1
    m2 = r
    pivot = arr[l]
    while i <= m2: 
        if arr[i] < pivot:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2

def quick_sort(arr, l, r):
    if l >= r: 
        return
    k = random.randint(l, r)
    arr[k], arr[l] = arr[l], arr[k]
    m1, m2 = partition3(arr, l, r)
    quick_sort(arr, l, m1 - 1)
    quick_sort(arr, m2 + 1, r)  

quick_sort(arr, 0, len(arr)-1)
for i in arr:
    print(i, end=" ")