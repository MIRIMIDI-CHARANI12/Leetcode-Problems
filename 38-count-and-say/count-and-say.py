class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        prev="1"
        for _ in range(2,n+1):
            res=""
            c=1
            for i in range(1,len(prev)):
                if prev[i]==prev[i-1]:
                    c+=1
                else:
                    res+=str(c)+prev[i-1]
                    c=1
            res+=str(c)+prev[-1]
            prev=res
        return prev
        