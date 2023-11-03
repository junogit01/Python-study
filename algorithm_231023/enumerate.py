colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

enum_colors = enumerate(colors)

# enumerate()를 사용하면 '인덱스를 포함한' enumerate 객체가 반환된다.
print(colors)
print(list(enum_colors))

# enumerate()를 활용하면, 인덱스와 값을 깔끔하게 처리할 수 있다.
for i, c in enumerate(colors):
    print(i, c)