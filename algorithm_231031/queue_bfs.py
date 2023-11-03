my_graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

from collections import deque

def queue_bfs(start_v):
    discovered = [start_v] # 결과 리스트 생성
    queue = deque([start_v]) # 큐 생성
    # 큐가 비어질 때까지 반복 
    # 큐에서 pop하고,
    # 연결된 노드가 결과에 없는 값이면, 결과 리스트에 추가
    # 연결된 노드를 큐에도 추가
    while queue:
        v = queue.popleft()
        for w in my_graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(queue_bfs(1))
