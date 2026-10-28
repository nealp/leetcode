from collections import deque
class Solution(object):
    def orangesRotting(self, grid):

        def rotting(queue, fresh):
            minutes = 0
            directions = [
                (-1,0) , (1,0) , (0,-1) , (0,1)
            ]
            while queue:
                curFresh = fresh
            #pop the index we processing
            #levels array
                #we are exploring each rotting oragne by level
                for _ in range(len(queue)):
                #add the neighboring cells wihtin 1 distance
                    r , c = queue.popleft()
                    for dr , dc in directions:
                        nr , nc = r+dr, c+dc
                        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        #rot the organe and add to queue
                            fresh -= 1
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                        
                    #pop the rotting orange from queue for this level
                    #after all the directions
                if curFresh != fresh:

                    minutes += 1
            if fresh != 0:
                return -1
            return minutes


                        

                
    


            
                    

            

             
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
      
        minutes = rotting(queue , fresh)
        return minutes



        
