class MyException(Exception):
    def __init__(self):
        super().__init__(self, "예상치 못한 답변으로 에러가 발생했습니다.")
        
select = input("파이썬이 재미있으면 1번, 아니면 2번")
if select == '1':
    print("파이썬은 역시 재미있어요")
elif select == '2' :
    raise MyException
else: print("1번과 2번만 입력하세요")