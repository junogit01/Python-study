def sum(*nums):
    result = 0
    for i in nums:
        result += i
    print(result)
    
sum(1,2,3,4)

def hello_player(**players):
    for key in players:
        print(f"{key}의 포지션은 {players[key]}")
    
hello_player(손흥민 = 'FW', 이강인 = 'MF', 황희찬 = 'MF')
        