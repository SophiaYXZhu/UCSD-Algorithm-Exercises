def common_seq(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    table = [[None]*(m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif seq1[i-1] == seq2[j-1]: # when there is a match (common seq)
                table[i][j] = table[i-1][j-1] + 1
            else: # insertion / deletion based on maximum length of current common seq
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[n][m]

n = int(input())
seq1 = [int(i) for i in input().split()]
m = int(input())
seq2 = [int(i) for i in input().split()]
print(common_seq(seq1, seq2))