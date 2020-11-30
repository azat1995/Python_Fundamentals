data=open('nums.txt', 'w')
nums=input()
data.write(nums)
nums=nums.split()
print(nums)

for i in range(len(nums)):
    nums[i]=int(nums[i])
print (sum(nums))
data.close()