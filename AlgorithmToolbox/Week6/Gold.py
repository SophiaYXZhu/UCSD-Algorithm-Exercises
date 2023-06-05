def find_max_weight(gold_weights, W):
    n = len(gold_weights)
    table = [[0 for i in range(n + 1)] for j in range(W + 1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            table[w][i] = table[w][i-1]
            if gold_weights[i-1] <= w:
                weight = table[w-gold_weights[i-1]][i-1] + gold_weights[i-1]
                if table[w][i] < weight:
                    table[w][i] = weight
    return table[W][n]

W, n = (int(i) for i in input().split())
gold_weights = [int(i) for i in input().split()]
print(find_max_weight(gold_weights, W))