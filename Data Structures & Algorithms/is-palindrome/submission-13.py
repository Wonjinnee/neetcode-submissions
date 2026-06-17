class Solution:
    def isPalindrome(self, s: str) -> bool:
        # change the string to lower case
        s = s.lower()
        # two pointers -> analyze symmetry by L and R
        L, R = 0, len(s)-1
        '''
        모르겠는것:
        1. if L or R is non-alphanumeric characters, ignore them.. 이거 어떻게 하지..?
        -> internet says to use .isalnum() function

        2. lower case로 바꾸는 것 <- 이것이 1차 시도에서 햇깔린 것 
        -> .lower()
        '''
        # when L == R happens, it means they scanned all the strings
        while L < R:
            # if they are non-alphanumeric characters, update
            if not s[L].isalnum():
                L += 1
                continue  # 이 줄이 핵심!
            if not s[R].isalnum():
                R -= 1
                continue  # 이 줄이 핵심!
            # if s[L] == s[R] -> if same, increment
            if s[L] == s[R]:
                L += 1
                R -= 1
            # else, return False
            else:
                return False
        # if the while loop ended, it means, it was palindrome
        return True
        
