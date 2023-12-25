# dp 로 해결


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == "0" :
            return 0
        elif len(s) == 1:
            return 1

        s_size = len(s)

        dp = [0 for _ in range(s_size+1)]
        dp[s_size] = 1
        end = s_size - 1


        for i in range(end, -1, -1):
            if s[i] == "0":
                continue

            if i + 1 <= s_size :
                dp [i] = dp[i+1]
            if i+ 2 <= s_size:
                if s[i:i+2] <= "26":
                    dp [i] += dp[i+2]

    
        return dp[0]
        


        
