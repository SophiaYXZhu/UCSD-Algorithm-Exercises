n = int(input())

if n == 0:
    print(n)
    exit(0)

digit_arr = [1, 1, 4, 9, 5, 4, 9, 1, 6, 5, 1, 6, 9, 9, 0, 9, 9, 6, 1, 5, 6, 1, 9, 4, 5, 9, 4, 1, 1, 0, 1, 1, 4, 9, 5, 4, 9, 1, 6, 5, 1, 6, 9, 9, 0, 9, 9, 6, 1, 5, 6, 1, 9, 4, 5, 9, 4, 1, 1, 0]

m = n % 60
sum_digits = 0
for i in range(0, m):
    sum_digits += int(digit_arr[i % 60])
print(int(str(sum_digits)[-1]))