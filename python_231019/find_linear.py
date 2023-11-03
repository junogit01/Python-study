nums = [int(x) for x in input().split()]
val = int(input())

result = []
def find_my_number(list, value) :  
    length = len(list)
    for i in range(length) :
        if value == list[i] :
            result.append(i)

find_my_number(nums, val)        
print(result)