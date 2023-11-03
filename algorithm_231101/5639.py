import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한을 늘려줘서 런타임 에러를 방지

tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

def order_change(s_idx, e_idx):
    if s_idx > e_idx:
        return
    d_idx = e_idx + 1
    # 루트 노드보다 큰 노드가 나오면 그 노드를 기준으로 왼쪽, 오른쪽 서브트리를 나눈다.
    for i in range(s_idx + 1, e_idx + 1):
        if tree[s_idx] < tree[i]:
            d_idx = i
            break
    order_change(s_idx + 1, d_idx - 1)
    order_change(d_idx, e_idx)
    print(tree[s_idx])
    
order_change(0, len(tree) - 1)