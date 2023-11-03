students = [
"강윤서",
"김민경",
"김태호",
"박강인",
"박준용",
"성지현",
"송형기",
"심은지",
"연제헌",
"이동준",
"이시헌",
"이준호",
"이호성",
"전소영",
"주나현",
"최은지"
]

import random

ran_num = random.randint(0, len(students)-1)
print(students[ran_num])