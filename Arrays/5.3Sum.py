def threeSum(a,k):
    res = []
    if len(a)<3 or a[0]==0:
        return res
    
    for i in range(len(a)):
        s = set()
        currSum = k-a[i]
        for j in range(i+1,len(a)):
            temp = currSum-a[j]
            if(temp in s):
                res.append([a[i],a[j],temp])
            s.add(a[j])
    return res

    



inp = int(input())
for _ in range(inp):
    k = int(input("Enter sum:"))
    a = list(map(int, input().rstrip().split()))
    print(threeSum(a,k))