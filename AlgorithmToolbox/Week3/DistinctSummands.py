n = int(input())

sums = 0
numbers = []
for i in range(1, n+1):
    numbers.append(i)
    sums += i
    if sums >= n:
        break

if sum(numbers) > n:
    numbers.pop(-1)
    numbers.pop(-1)
    numbers.append(n - sum(numbers))
print(len(numbers))
for i in numbers:
    print(i, end=" ")