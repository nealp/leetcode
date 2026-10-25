class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def bfs(r,c):

            area= 0
            #get queues row and col index
            queue = deque([(r,c)])

            #mark explpored
            grid[r][c] = 0
            while queue:

                r,c = queue.pop()
                area += 1

                directions = [ 
                    (1,0) , (-1,0) , (0,1) , (0,-1)
                ]

                for dr , dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr,nc))

                        
            return area

        
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea,area)
        
        return maxArea





            
            

            
            

            
            
            




        
