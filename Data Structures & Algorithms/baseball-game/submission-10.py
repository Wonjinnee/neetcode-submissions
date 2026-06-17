class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # make an array to store elements
        #  we need to use check every element
        #  therefore, use for loop 
        for i in operations: 
            # if the element is C
            if i == "C" :
                stack.pop()
            # if the element is D
            elif i == "D" :
                new = 2* int(stack[-1])
                stack.append(new)
            elif i == "+":
                new = stack[-1] + stack[-2]
                stack.append(new)
            # else, which would be int, just append the input 
            else:
                stack.append(int(i))
        
        # return the sum of the arrays
        return sum(stack)

            
