# 변수 이름만 바꿔주는 형태 (동일한 참조)
list_a = ["HTML", "CSS", "JS"]
list_b = list_a
list_b.append("python")
print(list_a, list_b)

# 얇은 복사
list_c = [["Programming", "Bored"], "HTML", "CSS", "JS"]
list_d = list_c.copy() # list_c.[:]
list_d.append("python")
print(list_c, list_d)
list_d[0][1] = ["Interesting"]
print(list_c, list_d)

# 깊은 복사
import copy
list_e = [["Programming", "Bored"], "HTML", "CSS", "JS"]
list_f = copy.deepcopy(list_e)
list_f.append("python")
print(list_f, list_e)
list_f[0][1] = ["Interesting"]
print(list_f, list_e)