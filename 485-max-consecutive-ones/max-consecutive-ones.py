class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        MaxCount = 0

        for i in nums:
            if i == 1:
                count +=1
            else:
                MaxCount = max(count,MaxCount)
                count = 0
        return max(MaxCount,count)
        