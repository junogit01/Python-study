def find_my_number(list, value):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if value == list[mid]:
            return mid
        elif value > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

result = find_my_number([1,2,4,5,6,7,8,9,10,11,12,13], 4)
print(result)