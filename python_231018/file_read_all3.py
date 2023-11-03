f = open("hello_10.txt", 'r')
data = f.read() # read()는 파일 내용을 한 번에 모두 읽어서 가져옵니다.
print(data)
f.close()