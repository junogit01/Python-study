def get_user_number(start, end):
    user_number = int(input(f"{start}부터 {end}까지의 숫자를 넣어주세요"))
    if user_number > 31 or user_number < 1 :
        raise Exception(f"숫자의 범위를 초과했습니다.")
    return user_number

def up_down_game():
    import random
    random_number = random.randint(1, 31) 
    try :
        while True :
            user_input = get_user_number(1, 31)
            if user_input == random_number :
                print('축하합니다~! 정답입니다!!!')
                break
            
            elif user_input < random_number :
                print('up\n')
            else :
                print('down\n')
    except Exception as e:
        raise Exception(e)
    
try :
    up_down_game()
except Exception as e:
    print(e)