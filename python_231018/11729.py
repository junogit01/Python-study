# def hanoi(num):
#     if num == 1:
#         return 1
#     return 2 * hanoi(num-1) + 1

def hanoi_detail(num, start, mid, end):
    if num == 1:
        print(start, end)
        return
    hanoi_detail(num-1, start, end, mid)
    print(start, end)
    hanoi_detail(num-1, mid, start, end)

number = int(input())
print(2 ** number - 1)
hanoi_detail(number, 1, 2, 3)