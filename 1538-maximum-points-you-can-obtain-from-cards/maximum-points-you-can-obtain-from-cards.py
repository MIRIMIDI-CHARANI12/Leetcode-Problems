class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        ts=sum(cardPoints)
        windowsize=n-k
        ws=sum(cardPoints[:windowsize])
        ms=ws
        for i in range(windowsize,n):
            ws+=cardPoints[i]-cardPoints[i-windowsize]
            ms=min(ms,ws)
        return ts-ms
        