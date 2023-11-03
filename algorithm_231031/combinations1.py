n, k = [5, 4]

def combine(n, k):
    combinations = []
    combi = []
    def dfs(k, start_v, combi):
        if k == 0:
            combinations.append(combi.copy()) # !!!
            return
        for i in range(start_v, n+1):
            combi.append(i)
            dfs(k - 1, i + 1, combi)
            combi.pop()
    dfs(k, 1, combi)
    return combinations

print(combine(n, k))