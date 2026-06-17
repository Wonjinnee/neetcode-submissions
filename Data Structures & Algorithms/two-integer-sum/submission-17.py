class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        6/30 복습
        sol1. brute force
        sol2. hash!!!
            hash면 element확인이 O(1)!
        
        안 좋은 습관
        1. array 를 sorting하려고 하는 강박 .. -> 상황을 파악해야
            * 이 문제는 index를 return해야함 -> 그러기에 
        '''
        # hash map -> number:index
        hashmap = {}
        # use enumerate! 
        for idx, num in enumerate(nums):
            want = target-num
            if want in hashmap:
                return [hashmap[want],idx]
            # key: num; value: idx
            hashmap[num] = idx



        