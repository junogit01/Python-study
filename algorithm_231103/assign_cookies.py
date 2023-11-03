def findContentChildren(self, g: list[int], s: list[int]) -> int:
    g.sort() # 사람 정렬
    s.sort() # 쿠키 정렬
    # 오름차순으로 정렬해서 조금이라도 해당되는 아이에게 먼저 주기
    i, j = 0 # 인덱스용 변수 선언
    while i < len(g) and j < len(s): # 사람이 더 있을 순 엇기에 i가 g의 총 길이보다 작으면서 쿠키도 추가로 가진게 아니기에 s의 길이보다 작아야한다.
        if s[j] >= g[i]: # 원하는 것보다 크기가 같거나 커버리면 바로 줘버린다.
            i += 1 # i증가해서 다음 사람이 받을 수 있도록 한다.
        j += 1 # 주고나서 j 증가시켜 다음 쿠키를 줄 수 있도록 한다.
    return i