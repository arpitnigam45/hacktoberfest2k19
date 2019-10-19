
nums = [3, 5, 2, 9, 101, 333, 4]
while len(nums):
    if(len(nums)==1):
        del(nums[0])
        break
    for i in range(len(nums)-1):
        if i%2==0:
            del nums[i]
    print(nums)
