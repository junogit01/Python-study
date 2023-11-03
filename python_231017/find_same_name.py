names = input().split()

s_no_same = set()
s_same = set()

for name in names:
    if name in s_no_same:
        s_same.add(name)
    else:
        s_no_same.add(name)

print(s_same)