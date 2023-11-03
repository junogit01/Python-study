# 백대열

def gcd(a:int, b:int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def baek_dae_yeol(n:int, m:int) -> None:
    gcd_num = gcd(n, m)
    print(f"{n//gcd_num}:{m//gcd_num}")
    

import sys
n, m = sys.stdin.readline().split(':')
baek_dae_yeol(int(n), int(m))