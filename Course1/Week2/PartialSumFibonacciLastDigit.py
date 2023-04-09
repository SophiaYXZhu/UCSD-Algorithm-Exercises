inp = input().split()
m, n = int(inp[0]), int(inp[1])
# m <= n

digit_arr = [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
a = m % 60 
b = n % 60

sum1 = 0 # m
sum2 = 0 # n

x = min(a, b)
y = max(a, b)
if a <= b:
    for i in range(a-1, b):
        sum1 += int(digit_arr[i % 60])
else:
    for i in range(b, a-1):
        sum1 += int(digit_arr[i % 60])
    sum1 = 280-sum1
print(int(str(sum1)[-1]))