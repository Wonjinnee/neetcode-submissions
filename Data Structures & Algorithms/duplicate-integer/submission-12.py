class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set the hash set
        hash_set = set()

        # use the for loop
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            hash_set.add(nums[i])
        return False
