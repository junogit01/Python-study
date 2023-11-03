nums = [1, 2, 3, 4]
# even_nums = []
# for i in nums:
#     even_nums.append(i * 2)

# -> 리스트 컴프리헨션 사용
even_nums = [i * 2 for i in nums]

print(even_nums)