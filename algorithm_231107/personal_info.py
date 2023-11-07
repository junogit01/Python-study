def cal_days(today):
    y, m, d = [int(i) for i in today.split('.')]
    return (y - 2000) * 28 * 12 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today_date = cal_days(today)
    for term in terms:
        name, period = term.split()
        terms_dict[name] = int(period)* 28
    for i, v in enumerate(privacies):
        collected_data, terms_id = v.split()
        if today_date >= cal_days(collected_data) + terms_dict[term_id]:
            answer.append(i + 1)
    # print(temrs_dict)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(today, terms, privacies)