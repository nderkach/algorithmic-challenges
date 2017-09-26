class Solution(object):
    def __init__(self):
        self.max_size = 0
    
    def get_square(self, matrix, srow, scolumn, size):
        if srow > len(matrix) - size or scolumn > len(matrix[0]) - size:
            return

                
        for row in range(srow, srow+size):
            for column in range(scolumn, scolumn+size):
                if matrix[row][column] == 0:
                    return
        
        print(srow, scolumn, size)
        self.max_size = max(size, self.max_size)
        
        self.get_square(matrix, srow, scolumn, size+1)
    
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        lmatrix = []
        for row in matrix:
            lmatrix.append([int(c) for c in row])
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if lmatrix[row][column] == 1:
                    self.get_square(lmatrix, row, column, 1)
                    
        return self.max_size * self.max_size
   
s = Solution()
print(s.maximalSquare(["10100","10111","11111","10010"]))