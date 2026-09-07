class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict = {}
        for i,num in enumerate(nums):
            if target-num in hashDict:
                return [hashDict[target-num],i]
            hashDict[num]=i