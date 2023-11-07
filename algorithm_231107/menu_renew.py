from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    cnt_orders = Counter(orders)
    print(cnt_orders)

    for i in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), i)
            temp += combi
        counter = Counter(temp).most_common()
        for i, v in counter:
            if v >= 2 and v == counter[0][1]:
                answer.append(''.join(i)
                )    
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

solution(orders, course)