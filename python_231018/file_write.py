f = open("hello_10.txt", "w")
for i in range(1, 10+1):
    f.write(f"Hello, No.{i} World!\n")
f.close