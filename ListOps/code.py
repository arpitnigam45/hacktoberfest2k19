'''
Task: Delete alternate elements of the given list, starting from index 0,
      print the list after each traversal.

Example: given list -> [1,2,3,4,5]
                o/p: [2, 4]
                     [4]
                     []

'''


nums = [3, 5, 2, 9, 101, 333, 4]
while len(nums):
    if(len(nums)==1):
        del(nums[0])
        break
    for i in range(len(nums)-1):
        if i%2==0:
            del nums[i]
    print(nums)
