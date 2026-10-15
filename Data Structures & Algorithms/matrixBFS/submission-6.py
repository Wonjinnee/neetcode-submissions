class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        '''
        What we know:
        (0,0) : start - top-left corner of the grid
        ROWS -1 , COLS - 1 - bottom-right corner 
        
        WTF : length of the shortest path -> need an variable to store the value of the length

        like any other search algoritm, we should have
        * visited : set of visited node
        * frontier : the nodes yet to visit - queue

        base case : return the length when we visit the goal
        edge case:
            - if out of bound
                if min(row, col) <= 0
                if row == ROWS or col == COLS
            - if it's rock
                if grid[row][col] == 1
        '''
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        goal = (ROWS -1, COLS - 1)
        length = 0
        # if the start is the rock
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        while queue: # while queue is not empty
                    # : if it's empty, there's no place to discover
            for i in range(len(queue)):
            # get the one to iterate in this loop
                r,c = queue.popleft()
                neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
                # if it reaches the goal, return 
                if (r,c) == goal:
                    return length
                
                for dr, dc in neighbors:
                    # edge cases : if they are out of bound
                    if (min(r + dr, c+ dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visited or 
                        grid[r+dr][c+dc] == 1 # if it's the island
                    ):  
                        continue # skip the iteration 
                    # if it's not the edge case
                    # add it to the queue
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr,c+dc))

            length += 1
        return -1






