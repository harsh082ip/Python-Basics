# loops

nums = [1, 2, 3, 4, 5]

# loop over a list

for num in nums:
    if num == 4:
        # break
        continue
    print(num)
    
# range
for i in range(len(nums)):
    print(nums[i])
    
for i in range (0, 11):
    print(i, end=' ')

# while loop
count = 0
while count <= 10:
    print(count)
    count+=1