# 구조 분해 할당 (destructuring assignment)
name, age = ['홍길동', 20]
odd, *even = [1, 2, 4, 8]
weight, _, height, _, address = [75, "TMI", 180.5, "TMI", "서울 중구"]
birthYear, *_, birthMonth = [2001, "TMI", "TMI", "TMI", 10]

print(f'name :{name}')
print(f'age :{age}')
print(f'odd :{odd}')
print(f'even :{even}')
print(f'weight :{weight}')
print(f'height :{height}')
print(f'address :{address}')
print(f'birthYear :{birthYear}')
print(f'birthMonth :{birthMonth}')