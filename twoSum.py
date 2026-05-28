class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_mapp = {}
        for i,num in enumerate(nums):
            if target-num in hash_mapp:
                return[hash_mapp[target-num],i]
            hash_mapp[num] = i