my_graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

def stack_dfs(start_v):
    discovered = [] # 결과 리스트 생성
    stack = [start_v] # 스택 생성
    # 스택이 비어질 때까지 반복
    # 스택에서 pop하고,
    # 결과에 없는 값이면, 결과 리스트에 추가
    # 연결된 노드를 스택에 추가
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in my_graph[v]:
                stack.append(w)
    return discovered

print(stack_dfs(1))