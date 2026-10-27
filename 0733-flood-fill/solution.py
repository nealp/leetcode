from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #no need to flood if they already match

        def flood(sr,sc,og):
            directions = [
                (1,0) , (-1,0) , (0,1) , (0,-1)
            ]

            queue = deque()
            queue.append((sr,sc))

            #you want to popo each row and change it
            #then check the neighboas to see if they are in the graph and if their color is same as the starting color
            while queue:
                r,c = queue.pop()
                image[r][c] = color

                for dr , dc in directions:
                    nr,nc = dr+r , dc+c
                #check that index is in range of graph and check that the explored cell is same as og color so we can flood it
                    if nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[0]) and image[nr][nc] == og:
                        queue.append((nr,nc))


        if image[sr][sc] == color:
            return image
    
        og = image[sr][sc]

        flood(sr,sc,og)
  
        return image

        
        
