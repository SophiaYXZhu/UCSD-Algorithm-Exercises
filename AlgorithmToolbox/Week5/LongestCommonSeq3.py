def common_seq(seq1, seq2, seq3):
    n = len(seq1)
    m = len(seq2)
    l = len(seq3)
    table = [[[None]*(l + 1) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(l + 1):
                if i == 0 or j == 0 or k == 0:
                    table[i][j][k] = 0
                elif seq1[i-1] == seq2[j-1] == seq3[k-1]: # when there is a match (common seq)
                    table[i][j][k] = table[i-1][j-1][k-1]+1
                else: # insertion / deletion based on maximum length of current common seq
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], \
                                      table[i-1][j-1][k], table[i][j-1][k-1], \
                                      table[i-1][j][k-1], table[i][j][k-1])
    return table[n][m][l]

n = int(input())
seq1 = [int(i) for i in input().split()]
m = int(input())
seq2 = [int(i) for i in input().split()]
l = int(input())
seq3 = [int(i) for i in input().split()]
print(common_seq(seq1, seq2, seq3))