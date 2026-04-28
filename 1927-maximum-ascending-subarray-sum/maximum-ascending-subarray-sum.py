class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        prev = 0
        largest_sum = 0
        sub_sum = 0
        i =0
        while i < len(nums):
            if prev < nums[i]:
                sub_sum += nums[i]
                prev = nums[i]
                i +=1
            else:
                largest_sum = max(largest_sum,sub_sum)
                sub_sum=0
                prev = 0


        return max(largest_sum,sub_sum)
                
        