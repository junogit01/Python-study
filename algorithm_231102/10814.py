import sys

n = int(sys.stdin.readline())
member = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member.append((age, name))

# new_member = sorted(member, key=lambda x:x[0])
# for i in new_member:
#     print(i[0], i[1])
    
member.sort(key=lambda x:x[0])
for i in member:
    print(i[0], i[1])