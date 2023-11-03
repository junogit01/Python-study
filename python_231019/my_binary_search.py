def find_number(nums:list, value:int) -> int:
    """
    이진 탐색을 통해 리스트의 특정 값의 위치를 반환

    Args:
        nums (list): 리스트
        value (int): 찾으려는 값

    Returns:
        int: 특정 값의 위치, 리스트에 특정 값이 없으면 -1을 반환
    """
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if value > nums[mid]:
            left = mid + 1
        elif value < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1