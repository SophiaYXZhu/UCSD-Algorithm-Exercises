n = int(input())

def compute_table(n, coins): # d = [1, 3, 4]
    table = [0 for i in range(n+1)]
    for m in range(1, n+1):
        table[m] = float("inf")
        for coin in coins:
            if m >= coin:
                num_coins = table[m-coin] + 1
                if num_coins < table[m]:
                    table[m] = num_coins
    return table[n]

print(compute_table(n, [1,3,4]))