class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
        6/15/26 진도
        Hashmap = map = dictionary = {}
        
        '''
        preMap = {} # value : index

        for i, n in enumerate(nums): # enumerate will make a collection of index and its value
            diff = target - n # chech whether the difference is already in the hash map
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n]= i
            
