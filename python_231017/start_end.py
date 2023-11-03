nums = list(input("").split())

# start, *_,end  = nums
start= nums.pop(0) # nums[0]
end = nums.pop() # nums[-1]

result = int(start) + int(end)
print(result)