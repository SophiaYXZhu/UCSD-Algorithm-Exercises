n = int(input())

numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

def is_better(a, b): # is a "greater than" b
    if b == -1:
        return True
    new1 = int(str(a)+str(b))
    new2 = int(str(b)+str(a))
    if new1 > new2:
        return True
    return False

salary = ""
while len(numbers) > 0:
    max_num = -1
    for num in numbers:
        if is_better(num, max_num):
            max_num = num
    salary += str(max_num)
    numbers.remove(max_num)

print(salary)