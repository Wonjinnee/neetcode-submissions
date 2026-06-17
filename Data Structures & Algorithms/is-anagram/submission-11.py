class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 있는지 확인하는 것 -> hashmap
        # sort -> 
        s_sort = sorted(s)
        t_sort = sorted(t)
        if s_sort == t_sort:
            return True
        return False
