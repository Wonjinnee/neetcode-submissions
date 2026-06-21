# 6/21 풀이 
class MinStack:
    '''
    main problem : the run time of getMin should be in O(1)
    => idea: make a two stack
    
    def __init__(self):
        self.stack = []
        minstack.stack = [] # 이 문법 잘 모르겠음
        minstack.append(float("inf"))

    def push(self, val: int) -> None:
        self.stack.append(val)
        minstack.append(min(minstack[len(minstack)-1], val)) # push the new minimum at the minstack

    def pop(self) -> None:
        self.stack.pop()
        minstack.pop()

    def top(self) -> int:
        return self.stack[len(self) - 1]

    def getMin(self) -> int:
        return minstack[len(self) - 1]
    '''
    # 틀.이 : python class 이해 부족 self.
    '''
    1. list[-1] : indicate the last element of the list
    '''
    def __init__(self):
        self.stack = []
        self.minstack = [] # 이 문법 잘 모르겠음
        self.minstack.append(float("inf"))

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.minstack.append(min(self.minstack[len(self.minstack)-1], val)) # push the new minimum at the minstack
        val = min(val, self.minstack[-1])
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
