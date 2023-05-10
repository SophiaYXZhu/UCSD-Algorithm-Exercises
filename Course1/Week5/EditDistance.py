def edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)
    table = [[x] + [0] * (m) for x in range(n+1)]
    table[0] = [x for x in range(m+1)]
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion_cost = table[i][j-1]+1
            deletion_cost = table[i-1][j]+1
            match_cost = table[i-1][j-1]
            mismatch_cost = table[i-1][j-1]+1
            if word1[i-1] == word2[j-1]:
                table[i][j] = match_cost
            else: 
                table[i][j] = min([insertion_cost, deletion_cost, mismatch_cost])
    return int(table[n][m])

word1 = input()
word2 = input()
print(edit_distance(word1, word2))