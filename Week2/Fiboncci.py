n = int(input())

if n == 0:
    print(0)
    exit(0)
    
arr = [0 for i in range(n+1)]
arr[0] = 0
arr[1] = 1
for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n])