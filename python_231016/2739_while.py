# while문으로 만드는 구구단
# "2 * 1 = 2" ... "2 * 9 = 18"

dan = int(input())

i = 1
while i <= 9:
    print(f'{dan} * {i} = {dan * i}')
    i += 1
    # print(dan, "*", i, "=", dan * i)
    # print("%d * %d = %d" % (dan, i, dan * i))