def threeSum(a,k):
    for i in range(len(a)):
        s = set()
        currSum = k-a[i]
        for j in range(1,len(a)):
            if(currSum-a[j]) in s:
                return [a[i],a[j],currSum-a[j]]
            s.add(a[j])
    return False



inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(threeSum(a,n))