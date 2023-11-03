# 클래스의 생성
class Animal:
    # "생성자"를 통한 객체 초기화
    def __init__(self):
        self.name = "unnamed"
        self.age = 0
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

# 클래스를 활용한 객체 생성
pig = Animal()
pig.name = "돼지"
pig.age = 10

panda = Animal()
pig.info()
panda.info()