my_graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v) # 결과에 추가
    for w in my_graph[v]: # 밸류로 반복해서, 결과에 없는 값이면 재귀함수 호출
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered # 결과 반환

print(recursive_dfs(1))