class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hash map
        # sort the list
        sorted(nums)
        # use the dictionary 
        freq = {}
        # output list
        output = []
        for i, j in enumerate(nums):                          
            # if nums[i] is not in freq, set the value as 1
            if nums[i] not in freq:
                freq[nums[i]] = 1
            # else, increase the frequency
            else:
                freq[nums[i]] += 1
        # compare the values and sort them by the value
        sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # use the for loop to append the key at the output
        for i in range(k):
            output.append(sorted_nums[i][0])
        # return the output
        return output
                

