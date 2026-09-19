class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,j = 0,1
        for j in range(len(nums)):
            if nums[j] != nums[a]:
                nums[a+1]=nums[j]
                a+=1
            
        return a+1
            
        