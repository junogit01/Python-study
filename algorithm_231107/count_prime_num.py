# n = 437674 
# k = 3
# result = 3

def solution(n,k):
    answer = 0
    word = []
    # 진법 변환
    while n:
        word += str(n % k) + word
        n //= k

    primes = [int(i) for i in word.split("0") if i != '']

    for i in primes:
        if i < 2:
            continue
        prime = True
        # 소수의 기준 = 약수가 1과 자기 자신 뿐
        for j in range(2, int(i**0.5) + 1 ):
            if i % j == 0:
                # 아 소수 아니네
                prime = False
                break
        if prime:
            answer += 1
    return answer

n = 437674
k = 3
print(solution(n,k))