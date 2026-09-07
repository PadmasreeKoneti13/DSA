class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h_s = set()
        for num in nums:
            if num in h_s:
                return True
            h_s.add(num)
        return False
        