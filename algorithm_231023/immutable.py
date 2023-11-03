str = 'apple'
print(id(str))

str = 'orange'
print(id(str))

# 실제 문자열은 한 번 생성된 후에 변경될 수도 없고, 변경된 적도 없다!!!
print(id('apple'), id('orange'), id(str))

# str[0] = "p" # 불변시퀀스 맞죠~!?