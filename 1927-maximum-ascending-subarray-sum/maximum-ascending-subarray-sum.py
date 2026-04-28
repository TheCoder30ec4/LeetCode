class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        curr = largest = nums[0]

        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                curr += nums[i]
            else:
                largest = max(largest,curr)
                curr = nums[i]  


        return max(largest,curr)
                
        