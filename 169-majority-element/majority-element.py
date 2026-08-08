class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        slow = 0
        count = 1
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                count = 1
            if count > n/2:
                return nums[i]