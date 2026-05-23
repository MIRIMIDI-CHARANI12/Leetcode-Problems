class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=[0]*n
        s=[0]*n
        ans=[0]*n
        p[0]=nums[0]
        for i in range(1,n):
            p[i]=p[i-1]*nums[i]
            s[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            s[i]=s[i+1]*nums[i]
            ans[0]=s[1]
            ans[n-1]=p[n-2]
        for i in range(1,n-1):
            ans[i]=p[i-1]*s[i+1]
        return ans


        
        