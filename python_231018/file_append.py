f = open("hello_10.txt", "a", encoding="utf-8")
for i in range(11, 11+10):
    data = f"안녕, 파이썬 No.{i}\n"
    f.write(data)
f.close()