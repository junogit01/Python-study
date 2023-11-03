def quick_sort(arr):
    lo = 0
    hi = len(arr)-1
    def sort(arr, lo, hi):
        if lo >= hi:
            return arr
        pivot = arr[lo]
        lt = lo + 1
        rt = hi
        
        while lt <= rt:
            # (피벗을 제외한) 배열 범위 안에 left 포인터가 있고, left 포인터에 있는 값이 피벗보다 커야한다.
            # 작으면 우측으로 이동
            while lt <= hi and arr[lt] <= pivot:
                lt += 1
            # (피벗을 제외한) 배열 범위 안에 right 포인터가 있고, right 포인터에 있는 값이 피벗보다 작아야한다.
            # 크면 좌측으로 이동
            while rt > lo and arr[rt] >= pivot:
                rt -= 1
            
            # 더 이상 움직일 수 없는 Left, Right
            if lt > rt: # Left와 RIght 위치가 바뀐 상태면
                arr[lo], arr[rt] = arr[rt], arr[lo] # Right와 Pivot에 있는 값을 스왑
            else: # Left와 RIght 위치가 적절하면
                arr[lt], arr[rt] = arr[rt], arr[lt] # Right와 Left에 있는 값을 스왑
        
        # 양쪽 퀵 정렬 (재귀)
        sort(arr, lo, rt - 1)
        sort(arr, rt + 1, hi)
    sort(arr, lo, hi)
    
arr = [6, 5, 2, 1, 3, 7, 9, 8]
quick_sort(arr)
print(arr)