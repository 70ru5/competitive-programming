class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
                k += 1
            
        while i < len(nums):
            nums[i] = "_"
            i += 1

        return k