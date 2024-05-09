class Solution(object):
    def scoreOfString(self, s):
        a=[]
        sum=0
        for i in s:
            a.append(ord(i))
        for i in range(0,len(a)-1):
            b=a[i]-a[i+1]
            if(b<0):
                b=a[i+1]-a[i]
            sum=sum+b
        return sum
S=Solution()
res=S.scoreOfString("hello")
print(res)