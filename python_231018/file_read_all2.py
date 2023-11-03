f = open("hello_10.txt", 'r')
for line in f: # f는 반복가능한 객체(iterable)로 사용된다.
    print(line.strip())
f.close()