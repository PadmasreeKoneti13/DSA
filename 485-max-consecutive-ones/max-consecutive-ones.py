class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                length  = 0
            max_length = max(length,max_length)
        return max_length