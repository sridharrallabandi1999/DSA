#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
	    n = len(matrix)
        INF = float('inf')  # Define a large number as infinity

        # Initialize matrix, replacing -1 with INF where there is no direct path
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = INF

        # Apply Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != INF and matrix[k][j] != INF:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # Replace INF with -1 to indicate no path exists
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == INF:
                    matrix[i][j] = -1
		#Code here


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends