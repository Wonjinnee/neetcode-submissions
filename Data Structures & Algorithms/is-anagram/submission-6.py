class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = {}
        freq = [[] for i in range(len(s)+1)]
        for i in s:
            scount[i] = 1+scount.get(i, 0)
        for n, c in scount.items():
            freq[c].append(n)
        
        tcount = {}
        freq = [[] for i in range(len(t)+1)]
        for i in t:
            tcount[i] = 1+tcount.get(i, 0)
        for n, c in tcount.items():
            freq[c].append(n)

        if scount == tcount:
            return True
        else:
            return False