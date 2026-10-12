class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # BASE CASE
        # 1. out of bound
        ROW, COL = len(grid), len(grid[0]) 
        visited = set() # visited is a list that records the visited nodes
        def bst(grid: List[List[int]], r:int, c: int, visited: set) -> int:
            if (min(r,c) < 0 or r == ROW or c == COL or
                grid[r][c] == 1 or (r,c) in visited): # if it's already visited, return 0
                return 0
            if r == ROW - 1 and c == COL - 1: # if we arrive to the destination, there's only one way
                return 1

            count = 0
            # record the current state
            visited.add((r,c))
            # travel 
            count += bst(grid, r-1, c, visited)
            count += bst(grid, r+1, c, visited)
            count += bst(grid, r, c-1, visited)
            count += bst(grid, r, c+1, visited)

            # remove the 
            visited.remove((r,c))

            return count
        
        return bst(grid, 0, 0, visited)

'''
    1차 풀이 오답노트:
    잘한 점: I got the base cases when I should return 0 correct
    못한 점: I forgot to add 'grid' as a parameter of the function
        visited = [] <- [] is a list! to use set, I should do visited = set()
        set a wrong starting point !! the return should be bst(grid, 0,0, visited) as we are starting from (0,0)
'''