#Counts how many numbers are smaller than the current number in a list
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smol = []
        for i in nums:
            count = 0
            for j in nums:
                if i >j:
                    count+=1
            smol.append(count)
            
        return smol
