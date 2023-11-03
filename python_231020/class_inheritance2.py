class Animal:
    def __init__(self):
        print("Animal 생성자가 호출됨")
        self.name = "unnamed"
        self.age = 0
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

class Human(Animal):
    def __init__(self):
        print("Human 생성자가 호출됨")
        self.job = "student"
        super().__init__() # 부모 클래스의 생성자를 호출합니다.
    def speak(self, data):
        print(f"{self.name} : {data}")
    def info(self): # 오버라이딩 : 부모클래스에 존재하는 함수와 동일한 이름의 함수를 자식클래스에서 재정의
        print(f"이름: {self.name}, 나이: {self.age}, 직업: {self.job}")
        
pig = Animal()
pig.name = "돼지"
pig.age = 5
pig.info()

choi = Human()
choi.name = "최인규"
choi.age = 20
choi.info()