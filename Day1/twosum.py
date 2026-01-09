nums=[2,9,15,18,27]
target = 11
sum = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
       sum  = nums[i]+nums[j]
       if sum == target:
        print(i,j)
        
