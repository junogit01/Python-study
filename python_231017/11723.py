s = set()

calc_count = int(input())
for _ in range(calc_count):
    calc = input().split()
    if calc[0] == "add":
        s.add(int(calc[1]))
    elif calc[0] == "remove":
        s.discard(int(calc[1]))
    elif calc[0] == "check":
        if int(calc[1]) in s: print(1)
        else: print(0)
    elif calc[0] == "toggle":
        if int(calc[1]) in s: s.discard(int(calc[1]))
        else: s.add(int(calc[1]))
    elif calc[0] == "all":
        s = set([i for i in range(1, 20+1)])
    elif calc[0] == "empty":
        s.clear()
    else :
        pass
        