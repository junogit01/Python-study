def trap(height: list[int]) -> int:
    water = 0
    lt = 0
    max_lt = height[lt]
    
    rt = len(height) - 1
    max_rt = height[rt]
    
    while lt < rt :
        # 만약에 왼쪽최대높이가 오른쪽최대높이보다 크면?
        # -> (최대왼쪽-현재왼쪽)을 물로 저장하고 왼쪽 이동 및 최대높이설정
        # 만약에 왼쪽최대높이가 오른쪽최대높이보다 작으면?
        # -> (최대오른쪽-현재오른쪽)을 물로 저장하고 오른쪽 이동 및 최대높이설정
        max_lt = max(height[lt], max_lt)
        max_rt = max(height[rt], max_rt)
        
        if max_lt <= max_rt:
            water += max_lt - height[lt]
            lt += 1
        else:
            water += max_rt - height[rt]
            rt -= 1
    return water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))