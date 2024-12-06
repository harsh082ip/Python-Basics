nums = [1, 2, 3, 4, 5]

# using constructor
nums2 = list((1, 2, 3, 4, 5))


print(nums, nums2)
print(nums[2])

# append
nums.append(6)
nums2.append("test")
print(nums)
print(nums2)

# insert into positions
nums.insert(2, 4)
print(nums)

# remove from list
nums.remove(4)
print(nums)

# remove by pos
nums.pop(3)
print(nums)

# nums.append("harsh")

# sort
nums.sort()
print(nums)

# sort reverse
nums.sort(reverse=True)
print(nums)

# change value
nums[0] = 18
print(nums)
