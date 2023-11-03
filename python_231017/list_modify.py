# 리스트의 수정

practice_list= [1, 2, 3, '파이', 'Apple', ['가', '나', '다', '라']]

# '파이'를 3.14로 수정!
practice_list[3] = 3.14
print(practice_list)

# 인덱싱과 슬라이싱의 차이 확인!
print(practice_list[2])
print(practice_list[2:3])

# practice_list[2] = [4 ,8] # 3을 [4, 8]로 수정! -> [1,2,[4,8],...]
practice_list[2:3] = [4 ,8] # [3]을 [4, 8]로 수정! -> [1,2,4,8,...]





# 리스트의 삭제
print(practice_list)

# practice_list[5:6] = [] # 'Apple'을 리스트에서 삭제(1)
del practice_list[5] # 'Apple'을 리스트에서 삭제(2)

# practice_list[5] = [] # 'Apple'을 []로 변경
print(practice_list)

del practice_list[-1][-1] # ['가', '나', '다', '라']에서 '라' 삭제
# practice_list[-1][-1:] = [] # ['가', '나', '다', '라']에서 '라' 삭제
print(practice_list)

practice_list[-1][1:] = [] # ['가', '나', '다']에서 '나', '다' 삭제
print(practice_list)