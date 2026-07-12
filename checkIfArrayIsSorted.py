nums = [10,20,20,30,40,50]
count = 1
for i in range(len(nums)-1):
    if nums[i] <= nums[i+1]:
        count += 1
if count == len(nums):
    print("sorted")
else:
    print("not sorted")