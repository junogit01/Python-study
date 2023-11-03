def divisor():
    try:
        num = int(input())
        print(100/num)
    except ValueError as e:
        print("숫자 형식으로 작성해주세요", e)
        divisor()
    except ZeroDivisionError as e:
        print("영으로 나눌 수 없습니다", e)
        divisor()
    except Exception as e:
        print(e, e.__class__)
    else:
        print("언제 실행될까요? -> try 블록이 정상적으로 무사히 실행되는 경우!")
divisor()