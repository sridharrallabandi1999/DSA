class Solution(object):
    def climbStairs(self, n):

        if n ==0:
            return 1
        if n ==1:
            return 1 
        if n==2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i]=dp[i-2]+dp[i-1]
            
        return (dp[n-1])