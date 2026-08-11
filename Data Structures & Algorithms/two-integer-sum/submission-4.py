class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            num1=target-nums[i]
            if num1 in seen:
                return[seen[num1],i]
            seen[num]=i

