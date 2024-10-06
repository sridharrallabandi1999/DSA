#User function Template for python3
from collections import deque
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        if start == end:
            return 0
        q= deque([(start,0)])
        
        dist = [float('inf')]*100000
        dist[start]=0
        mod = 100000
        
        while q:
            node,steps = q.popleft()
            
            for num in arr:
                new_num= (num*node) % mod
                
                if steps+1 < dist[new_num]:
                    dist[new_num]=steps+1
                    if new_num == end:
                        return steps+1
                    q.append((new_num,steps+1))
        return -1
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends