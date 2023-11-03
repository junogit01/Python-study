d_name = {}

names = input().split()
for name in names:
    if name in d_name:
        d_name[name] += 1
    else :
        d_name[name] = 1

s_result = set()

for k, v in d_name.items():
    if v >= 2:
        s_result.add(k)
        
print(s_result)