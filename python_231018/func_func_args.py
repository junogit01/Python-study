def robot_calc(calc_func):
    print("로봇계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력 : "))
    num2 = int(input("두번째 숫자를 입력 : "))
    result = calc_func(num1, num2)
    print(f"계산 결과는 {result}입니다.")
    
def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

robot_calc(plus)
robot_calc(minus)