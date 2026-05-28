class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #approach-2
        # dictionary = Counter(nums)
        # for key,val in dictionary.items():
        #     if val > 1:
        #         return True
        # return False

        #approach - 1
        # dictionary = {}
        # for num in nums:
        #     count = 0
        #     if num not in dictionary:
        #         count=1
        #         dictionary[num] = count
        #     else:
        #         count+=1
        #         dictionary[num] += count
        # for val in dictionary.values():
        #     if val > 1:
        #         return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False