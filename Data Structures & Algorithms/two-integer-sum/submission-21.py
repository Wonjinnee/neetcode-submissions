class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap to store the value and the index we already observed
        prevMap = {} 
        for i,n in enumerate(nums):
            want = target - n
            # if the previous element is not at the prevmap, 
            # add the element at the hashmap
            if want in prevMap:
                return [prevMap[want], i]
            prevMap[n] = i
            