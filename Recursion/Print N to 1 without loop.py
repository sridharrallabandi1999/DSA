#User function Template for python3

class Solution:
    def printNos(self, n):
        if n<=0:
            return
        print(n,end = ' ')
        return self.printNos(n-1)
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends