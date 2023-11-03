class Animal:
    def __init__(self):
        print("Animal 생성자가 호출됨")
        self.name = "unnamed"
        self.age = 0
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

# 자식 클래스에 생성자가 없는 경우에는 자동으로 부모 생성자를 호출합니다.
class Human(Animal):
    def speak(self, data):
        print(f"{self.name} : {data}")
        
pig = Animal()
pig.name = "돼지"
pig.age = 5

choi = Human()
choi.name = "최인규"
choi.age = 20

pig.info()
choi.info()
choi.speak("안녕하세요. 저는 사람입니다.")