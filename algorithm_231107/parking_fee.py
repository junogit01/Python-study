from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    park_info = defaultdict(list)
    #출입 기록하기
    for i in records:
        time, number, status = i.split()
        h, m = time.split(':')
        minute = int(h) * 60 + int(m)
        park_info[number].append(minute)
    
    park_fee = defaultdict(int)
    for k, v in park_info.items():
        if len(v) % 2 == 1:
            v.append(23 * 60 + 59)
        park_fee[k] = sum([v[i+1] - v[i] for i in range(len(v)) if i % 2 == 0])
    print(park_fee)
    answer = sorted(park_fee.items())
    for i in range(len(answer)):
        minute = answer[i][1]
        if minute <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + math.ceil((minute - fees[1]) / fees[2]) * fees[3]
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", 
           "06:00 0000 IN", 
           "06:34 0000 OUT", 
           "07:59 5961 OUT", 
           "07:59 0148 IN", 
           "18:59 0000 IN", 
           "19:09 0148 OUT", 
           "22:59 5961 IN", 
           "23:00 5961 OUT"]


print(solution(fees, records))