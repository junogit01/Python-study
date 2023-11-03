# 1) 함수를 변수에 담아서 사용하기
def print_something(something):
    print(something)

ps = print_something
ps("함수를 변수처럼 담아서 사용할 수 있어요!")

# 2) 함수를 리스트에 담아서 사용하기
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
calcs = [plus, minus]
print(calcs[0](10, 18))
print(calcs[1](10, 18))

# 2) 함수를 딕셔너리에 담아서 사용하기
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
d_calcs = {
        "더하기" : plus,
        "빼기" : minus
    }
print(d_calcs["더하기"](10, 18))
print(d_calcs["빼기"](10, 18))