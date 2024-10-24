#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        
        #smallest valid input
        if n == 0:
            return 0
        sum_n = n * (n + 1) // 2
        return sum_n**2
            
        #code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends