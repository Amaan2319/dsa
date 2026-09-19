class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], index]
            seen[num]=index

        return 

        