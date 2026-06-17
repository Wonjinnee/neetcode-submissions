class Solution:
    '''
    array 문제 
    encode 하며 str의 정보를 저장해야함 
    그 방법 중 하나가 int(len(str[i]))
    '''
    def encode(self, strs: List[str]) -> str:
        #set the output string
        output = ""
        #iterate by for loop
        for i in range(len(strs)):
            output = output+str(len(strs[i]))+'#'+strs[i]
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        i= 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+= 1
            size = int(s[i:j])
            j+=1
            output.append(s[j:j+size])
            i = j + size
        return output    

