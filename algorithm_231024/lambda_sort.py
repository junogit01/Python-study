# 정렬 함수는 두 가지 입니다.
# sort(), sorted()
# 리스트.sort() : 리스트를 정렬해준다. -> None
# sorted(리스트) : 리스트를 정렬해준다. -> 정렬된리스트

datas = ['서울 09:13:00', '서울 12:10:00', '부산 09:20:00', '서울 08:00:00', '대구 09:15:00']

# def alpha(x):
#     return x.split()[1]
# print(sorted(datas, key=alpha))
# print(sorted(datas, key=lambda x: x.split()[1]))

# def alpha(x):
#     return x.split()[1]
# datas.sort(key=alpha)
datas.sort(key=lambda x: x.split()[1])
print(datas)