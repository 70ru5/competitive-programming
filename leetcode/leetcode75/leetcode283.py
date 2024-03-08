#最初に考えたやつ

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = [i for i in nums if i == 0]
        not_zeroes = [i for i in nums if i != 0]

        nums = not_zeroes 

#提出したやつ
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_number = 0

        for num in nums:
            if num != 0:
                nums[index_number] = num
                index_number += 1
        
        while index_number < len(nums):
            nums[index_number] = 0
            index_number += 1