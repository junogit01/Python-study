f = open("hello_10.txt", 'r')
while True:
    line = f.readline() # readline은 더 이상 읽을 라인이 없으면 None을 반환합니다.
    if not line:
        break
    print(line.strip())
f.close()