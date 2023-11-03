# isinstance()

class Animal:
    def __init__(self):
        self.name = "unnamed"
        self.age = 0
        
class Human(Animal):
    def __init__(self):
        self.job = "student"
        super().__init__()
        
pig = Animal()
choi = Human()

# True / False
print(isinstance(pig, Animal)) # True
print(isinstance(pig, Human)) # False (pig는 Human과 관계없이 생성된 객체!)
print(isinstance(choi, Animal)) # True
print(isinstance(choi, Human)) # True

print(isinstance(pig, object)) # True
print(isinstance(choi, object)) # True