star = int(input())
for n in range(1, star * 2):
    if n <= star:
        # [n=1] 공백 4 / 별 1=(2n-1)
        # [n=2] 공백 3 / 별 3=(2n-1)
        # [n=3] 공백 2 / 별 5=(2n-1)
        # [n=4] 공백 1 / 별 7=(2n-1)
        # [n=5] 공백 0 / 별 9=(2n-1)
        print(" " * (star-n) + "*" * (2 * n -1))
    else:
        # n -> m
        m = 2 * star - n
        # [n=6]4 공백 1=(n-star) / 별 7= 2 * (2 * star - n) - 1
        # [n=7]3 공백 2=(n-star) / 별 5= 2m - 1
        # [n=8]2 공백 3=(n-star) / 별 3= 2m - 1
        # [n=9]1 공백 4=(n-star) / 별 1= 2m - 1
        print(" " * (n-star) + "*" * (2 * m - 1))

