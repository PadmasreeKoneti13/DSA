class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        for key,val in hash_map.items():
            if val > len(nums)//2:
                return key
        