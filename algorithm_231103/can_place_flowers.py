def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

    for position in range(len(flowerbed)):
        left, right = position - 1, position + 1  # left, right 위치 인덱스 설정
        if flowerbed[position] == 0 and (left < 0 or flowerbed[left] == 0) and (right >= len(flowerbed) or flowerbed[right] == 0):
            # 해당 인덱스의 값이 0이면서, left도 0이고 right가 0 이면?
            # 이러면 left,right에서 인덱스 에러나와서 추가로 left가 0보다 크면서, right는 flowerbed의 길이보다 작아야한다.
            # 인덱스가 첫 시작이 0이면 안되네? left 가 0 보다 크거나, right가 len 길이보다 큰것도 추가
            flowerbed[position] = 1 # 해당 인덱스 1 대입
            n -= 1 # n에서 1을 빼서 심어야 할 꽃의 개수 차감

        if n <= 0: # 만약 n이 0이면 더이상 심어야할 꽃이 없는 것이기에 n이 0일 때도 있기에 포함시켜줘야한다.
            return True # True 반환
    return False # 아니면 False 반환


def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for pos in range(len(flowerbed)):
        left, right = pos - 1, pos + 1
        if flowerbed[pos] == 0 and (left < 0 or flowerbed[left] == 0) and (right >= len(flowerbed) or flowerbed[right] == 0):
            flowerbed[pos] = 1
            n -= 1

        if n <= 0:
            return True
    return False