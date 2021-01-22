import json

def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    optimal_items = list()
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    res = table[n][W]
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][w]:
            continue
        else:
            optimal_items.append(wt[i - 1])
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return table[n][W],optimal_items


val = [50, 100, 150, 200]
wt = [8, 16, 32, 40]
W = 64

#print(knapSack(W, wt, val))
