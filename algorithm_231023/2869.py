# 달팽이는 올라가고 싶다.
import sys
import math

# snail1 -> 시간 초과
# def snail1() :
#     a, b, v = [int(x) for x in sys.stdin.readline().split()]
#     now, day = 0, 0

#     while now < v:
#         day += 1
#         now += a
#         if now >= v:
#             break
#         now -= b
#     print(day)

# snail1()

def snail2() :
    a, b, v = [int(x) for x in sys.stdin.readline().split()]
    
    everyday = a - b
    real_v = v - b
    
    day = math.ceil(real_v / everyday)
    # if real_v % everyday != 0:
    #     day += 1   
    print(day)
    
snail2()