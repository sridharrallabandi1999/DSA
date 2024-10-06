from typing import List
from collections import deque
class Solution:

   
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        dist = [float('inf')] * V
        dist[S] = 0
        
        
        q = deque([S])
        
        while q:
            u = q.popleft()
            
            
            for neighbor, weight in adj[u]:
                
                distance = dist[u] + weight
                
                
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    q.append(neighbor)
        
       
        return dist

       
    # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends