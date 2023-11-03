# 스페셜 메소드 : 앞뒤로 두 개의 언더스코어(_)가 붙은 변수 또는 메서드
# 특정한 상황에서 자동으로 호출됩니다. (스페셜 메소드명은 약속이 되어있습니다.)
# 파이썬의 표준 타입들과 유사하게 동작하는 클래스를 설계하기 위해서 반드시 필요합니다.

# 대표적인 스페셜 메소드 : __init__

class Car:
    # 자동차에는 차대번호(id) (ex. 123허4567)
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return "차대번호 : "+self.id

def main():
    my_car = Car("52러8445")
    print(len(my_car))
    print(str(my_car))

main()