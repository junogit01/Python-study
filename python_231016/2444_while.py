star = int(input())

# [n=1] 공백 4 / 별 1=(2n-1)
# [n=2] 공백 3 / 별 3=(2n-1)
# [n=3] 공백 2 / 별 5=(2n-1)
# [n=4] 공백 1 / 별 7=(2n-1)

n = 1
while n < star:
    print(f'{" " * (star-n)}{"*" * (2 * n -1) }')
    n += 1

# [n=5] 공백 0 / 별 9=(2n-1)
# [n=4] 공백 1 / 별 7=(2n-1)
# [n=3] 공백 2 / 별 5=(2n-1)
# [n=2] 공백 3 / 별 3=(2n-1)
# [n=1] 공백 4 / 별 1=(2n-1)
while n > 0:
    print(f'{" " * (star-n)}{"*" * (2 * n -1) }')
    n -= 1