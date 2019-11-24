class Solution(object):
    def setZeroes(self, matrix):
        points = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
        for i, a in enumerate(points):
            matrix[a[0]] = [0 for k in range(len(matrix[0]))]
            for k in range(len(matrix)): matrix[k][a[1]] = 0     