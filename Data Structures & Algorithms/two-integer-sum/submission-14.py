class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sol 1
        # # use the binary search
        # # medium
        # med = len(nums)//2
        # # if 2*med < 

        # sol 2
        # Hash map
        hash_map = {}
        # store the values of nums as a key and remainer as a value
        # if there exists a remainer at nums, return the key and value
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],i)
            if target-nums[i] in hash_map :
                j = hash_map[target-nums[i]]
                if i != j:
                    return [j,i]

        