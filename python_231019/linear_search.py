# 선형탐색(순차탐색)
def find_my_number(list, value) :
    for i, v in enumerate(list) :
        if value == v :
            return i
    return -1

result = find_my_number([5,2,6,1,2,3,4,7,9,1,5], 9)
print(result)