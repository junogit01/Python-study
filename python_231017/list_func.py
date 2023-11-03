# 리스트 관련 함수
names = ['이시헌', '김태호', '이동준']

# 리스트.append(요소) -> 리스트 맨 뒤에 요소를 추가한다.
names.append('최인규')
print(names)

# 리스트.insert(인덱스, 요소) -> 리스트 중 특정 인덱스에 요소를 삽입한다.
names.insert(1, '이준호')
print(names)

# 리스트.pop(인덱스) -> 리스트 중 특정 인덱스에 존재하는 요소를 꺼낸다.
# (인덱스를 생략하면 맨 뒤 요소를 꺼낸다)
popped_name = names.pop(2)
print("내가 꺼낸 요소는 --->", popped_name)
print(names)

# 요소 in 리스트 -> 리스트에 해당 요소의 존재 여부를 반환한다.
isPresent = '연제헌' in names
print(isPresent)

# 리스트.sort() -> 리스트를 오름차순으로 정렬한다.
names.sort()
print(names)

# 리스트.reverse() -> 리스트의 순서를 역순으로 뒤집는다.
names.reverse()
print(names)

# 리스트.extend(추가할리스트) -> 리스트의 맨 뒤에 추가할리스트가 확장된다.
names.extend(['김태호', '연제헌'])
print(names)

# 리스트.index(요소) -> 리스트 내 요소 위치를 반환한다.
# 만약 요소가 중복되는 경우, 첫 번째 위치를 반환한다.
idx = names.index('이준호')
print(f'요소 "이준호"의 위치는 {idx}이다')

# 리스트.count(요소)-> 리스트 내 같은 값을 가진 요소의 개수를 반환하다.
names.append('이준호')
names.append('이준호')
names.append('이준호')
print(names)
cnt = names.count('이준호')
print(f'리스트에서 "이준호"의 개수는 {cnt}이다')

# len(리스트)
length = len(names)
print(f'리스트의 총 길이는 {length}이다.')