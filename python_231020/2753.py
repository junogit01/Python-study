# 4의 배수 + 100의 배수면 윤년 X
# 4의 배수 + 100의 배수가 아니면 윤년 O
# 4의 배수 + 400의 배수면 윤년 O

# 1900 -> 4배수 O, 100의 배수 O, 400의 배수 X (윤년 X)
# 2000 -> 4배수 O, 100의 배수 O, 400의 배수 O (윤년 O)
# 2023 -> 4배수 X, 100의 배수 X, 400의 배수 X (윤년 X)
# 2024 -> 4배수 O, 100의 배수 X, 400의 배수 X (윤년 O)

def check_leap_year():
    try :
        year = int(input())
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(1)
        else:
            print(0)
    except ValueError as e:
        print(e) # ValueError 발생 시 어떻게 대처해야하는지 정의
        check_leap_year() # 내가 아는 에러... 다시 동작하도록 설정
    except Exception as e:
        print(e) # 내가 전혀 알지못하는 에러가 발생하면 어떻게 대처해야... [ex. 로그파일에 기록]

check_leap_year()
        
