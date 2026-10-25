class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)):
            num = nums[i]

            if i+1 == len(nums):
                continue
            nextNum = nums[i+1]
            if num %2 == 0:
                if nextNum %2 !=1:
                    return False
            elif num%2 == 1:
                if nextNum %2 != 0:
                    return False
        
        return True
            
            
        
