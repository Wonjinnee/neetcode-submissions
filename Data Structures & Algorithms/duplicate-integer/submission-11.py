class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sol 1. 
        already = []
        # sort the array
        nums.sort()
        for i in range(len(nums)):
            # check if nums[i] is in already
            if nums[i] in already:
                return True
            # if so, return True
            already.append(nums[i])
            # else, add the number at already
        # return false
        return False

