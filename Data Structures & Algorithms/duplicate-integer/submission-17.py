class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a new list that would contain all element
        new = [] 
        # use for-loop to loop through the object
        for i in nums:
            # if the element is in the new list, return false
            if i in new:
                return True
            # if the element is not in the new list, add the element in the list
            new.append(i)
        return False
