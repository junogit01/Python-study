# for문으로 만드는 구구단
# "2 * 1 = 2" ... "2 * 9 = 18"

dan = int(input())

for i in range(1, 9+1):
    print(f'{dan} * {i} = {dan * i}')
    # print(dan, "*", i, "=", dan * i)
    # print("%d * %d = %d" % (dan, i, dan * i))