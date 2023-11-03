def say_hello():
    nation = input("국적을 입력하세요 : ")
    if nation.lower() == 'korea':
        return hello_kor()
    else :
        return hello_eng()
    
def hello_kor():
    print("안녕하세요")
    
def hello_eng():
    print("Hello")
    
say_hello()