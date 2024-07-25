val = 2
nums = [0,1,2,2,3,0,4,2]
index = 0
for i in range(len(nums)):
    if nums[i] != val:
            nums[index] = nums[i]
            index += 1

print(index)
