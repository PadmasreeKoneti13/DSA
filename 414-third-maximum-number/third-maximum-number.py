class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums = [x for x in nums if x != first_max]
        if not nums:
            return first_max
        second_max = max(nums)
        nums = [x for x in nums if x != second_max]
        if nums:
            return max(nums)
        return first_max