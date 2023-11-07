from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score_dict = defaultdict(int)
    # kabti_dict = {
    #     1: ["R", "T"],
    #     2: ["C", "F"],
    #     3: ["J", "M"],
    #     4: ["A", "N"]
    # }

    # score_dict: {
    #     1: 3, # 네오형 3점 매우 비동의
    #     2: 2, # 네오형 2점 비동의
    #     3: 1, # 네오형 1점 약간 비동의
    #     4: 0, # 어떤 유형의 점수를 얻지 않음, 모르겠음
    #     5: 1, # 어피치형 1점 약간 동의
    #     6: 2, # 어피치형 2점 동의
    #     7: 3, # 어피치형 3점 매우 동의
    # }

    for i, v in enumerate(survey):
        print(choices[i],v)
        if 1 <= choices[i] <= 3:
            score_dict[v[0]] += 4 - choices[i]
        elif 5 <= choices[i] <= 7:
            score_dict[v[i]] += choices[i] - 4
    # if score_dict["R"] 
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5,3,2,7,5] 
print(solution(survey, choices))