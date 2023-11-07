

def solution(N, stages):
    answer = []

    # 실패율
    fail_rates = {} # 실패율 저장한 dict 선언
    
    # 도전자수
    people = len(stages) # 도전자수 구하기
    
    for i in range(1,N + 1):
        if people == 0: # 사람이 없으면 그냥 0으로 고정
            fail_rates[i] = 0
        else:
            count_i = stages.count(i)
            fail_rates[i] = count_i / people
            people -= count_i
    answer = sorted(fail_rates, key= lambda x: fail_rates[x], reverse=True)
    return answer


n = 5	
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
# [3,4,2,1,5]
print(solution(n, stages))
# n = 4
# stages = [4,4,4,4,4]
# # [4, 1, 2, 3]
# print(solution(n, stages))