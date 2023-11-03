import random

# 1~30까지 10개의 숫자를 random_nums.txt 파일에 입력
with open("random_nums.txt", "w") as f:
    for _ in range(10):
        rand_num = random.randint(1, 30)
        f.write(str(rand_num)+'\n')
        
# 숫자를 입력받고, 파일 안에 숫자가 있는지 확인해서 [위치 반환]
my_num = int(input())
result = []
with open("random_nums.txt", "r") as f:
    for k, v in enumerate(f):    
        real_num = int(v.strip())
        if my_num == real_num:
            result.append(k)
    if len(result) == 0:
        result.append(-1)
        
with open("random_nums_result.txt", "w") as f:
    for i in result:
        f.write(str(i) + '\n')