class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current_sum = sum(nums[:k])
        max_sum = current_sum 

        for i in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            print(current_sum)

            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum / k