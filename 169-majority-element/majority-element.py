class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candid = None
        count = 0
        for num in nums:
            if count == 0:
                candid = num
            if num == candid:
                count += 1
            else:
                count -= 1
        return candid