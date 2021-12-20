def threeSum(a,k):
    if a[0] and len(a)==1:
        return
    for i in range(len(a)):
        s = {}
        currSum = k-a[i]
        for j in range(1,len(a)):
            temp = currSum-a[j]
            if(temp in s):
                return [i,j,s[temp]]
            s[a[j]]= j

    



inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(threeSum(a,n))