import sys
'''
   11
    1 4
    3 5
    0 6
    5 7
    3 8
    5 9
    6 10
    8 11
    8 12
    2 13
    12 14 
    '''
# n = int(sys.stdin.readline().strip())
# meeting = []
# cnt = 0
# j = 1
# for i in range(n):
#     s, e =[int(i) for i in sys.stdin.readline().split()]
#     meeting.append([s, e])
# for i in range(len(meeting)):
#     if meeting[i][j] > meeting[j+i][i]:
#         continue
#     elif meeting[i][j] == meeting[j+i][i]:
#         continue
#     else:
#         cnt += 1

# print(cnt)
        

# n = int(sys.stdin.readline().strip())
# meeting = []
# cnt = 0

# for i in range(n):
#     s, e = [int(i) for i in sys.stdin.readline().split()]
#     meeting.append([s, e])

# for i in range(len(meeting)):
#     for j in range(i+1, len(meeting)):  # 다른 모든 회의와 비교
#         if meeting[i][1] >= meeting[j][0]:  # i번째 회의의 종료시간이 j번째 회의의 시작시간보다 늦을 때
#             pass
#         else:
#             cnt += 1

# print(cnt)

import sys
n = int(sys.stdin.readline().strip())

# 입력값을 통해 meeting 배열 완성
meeting = []
for _ in range(n):
    start, end = [int(i) for i in sys.stdin.readline().split()]
    meeting.append((start,end))
# meeting 배열 정렬 기준(1순위: 끝나는 시간, 2순위 : 시작시간)
# 2순위 추가 이유: 같은 시간에 끝나는 회의는 시작 시간이 빠른게 앞에 와야 한다.
meeting.sort(key=lambda x: (x[1], x[0]))

# meeting 배열에서 끝나는 시간을 기준으로 찾아와야 한다.
finish_time = 0
# 가능한 회의 개수
count = 0

for i in meeting:
    start_time, end_time = i
    if start_time >= finish_time: # finish_time과 가장 비슷하게 큰 회의를 가져온다.
        count += 1
        finish_time = end_time

print(count)