class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # get the number of rows and the colums
        ROWS, COLS = len(grid), len(grid[0])
        # make a queue to record your next destination
        queue = deque()
        # make a set that stores the visited nodes
        visited = set()
        # goal 
        goal = (ROWS - 1, COLS - 1)
        # record the starting position (0,0) - top left corner
        queue.append((0,0))
        visited.add((0,0))
        # a variable to store the length
        length = 0
        # if the starting is already 1, there's no such path, so return -1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1]:
            return -1
        # while queue is not empty
        while queue:
            for i in range(len(queue)):
                # get the current node we're trying to search
                r, c = queue.popleft()
                neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
                if (r,c) == goal:
                    return length
                # check all neighbors 
                for i in range(len(neighbors)):
                    dx ,dy = neighbors[i][0], neighbors[i][1]
                    # edge cases
                    # 1. if the move is out of bound, 2. 
                    if (min(r+dx, c + dy) < 0 or r+dx == ROWS or c + dy == COLS or (r+dx, c+dy) in visited or grid[r+dx][c+dy] == 1):
                        continue
                    queue.append((r+dx, c+dy))
                    visited.add((r + dx,c + dy))
            length += 1
        
        return -1
