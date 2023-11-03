import random
random_number = random.randint(1, 30) 

while True :
    user_input = int(input("맞춰보세요(1~30) : "))
    if user_input == random_number :
        print('축하합니다~! 정답입니다!!!')
        break
    elif user_input > 30 or user_input < 1 :
        print('범위 안의 숫자를 입력해주세요\n')
    elif user_input < random_number :
        print('up\n')
    else :
        print('down\n')