class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        blu = len(nums)-1
        red,checker = 0,0
        
        while checker <= blu:
            if nums[checker] == 0:
                nums[checker],nums[red] = nums[red],nums[checker]
                checker +=1
                red +=1
                
            elif nums[checker] == 1:

                checker +=1
            else:
                nums[blu],nums[checker] = nums[checker],nums[blu]
                blu -= 1
