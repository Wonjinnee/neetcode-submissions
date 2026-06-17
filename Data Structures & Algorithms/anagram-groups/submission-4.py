class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop
        # hash map : key: sorted characters; value: list of anagrams

        hash_map = {}
        for i in range(len(strs)):
            # if there exists an anagram, 
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in hash_map:
                # append the word to the list
                hash_map[sorted_str].append(strs[i])
            # if there does not exist an anagram, make the anagram a key and
            # set the word the value of the key
            else:
                hash_map[sorted_str] = [strs[i]]
        # finally print out the values of the hash map <- how?
        return list(hash_map.values())


