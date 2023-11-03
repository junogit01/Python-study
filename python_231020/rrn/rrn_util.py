# 사용자가 정의한 모듈
# print("rrn_util -> ", __name__)

def refine_data(data):
    data = data.replace(" ", "").replace("-", "")
    if len(data) != 13:
        return
    return data

def gender(data)-> str:
    data = refine_data(data)
    gender_num = int(data[-7])
    if gender_num % 2 == 0:
        return "여자"
    return "남자"

def birth(data) -> (int, int, int):
    data = refine_data(data)
    year = int(data[0:2])
    month = int(data[2:4])
    day = int(data[4:6])
    gender_num = int(data[-7])
    if gender_num < 3 :
        year += 1900
    else :
        year += 2000
    return year, month, day

if __name__ == "__main__":
    rrn_nums = input("주민번호를 입력하세요!")
    print(gender(rrn_nums))
    print(birth(rrn_nums))